import sys
sys.dont_write_bytecode = True

from config import *
from cards import *
from active_player import *
from functions import *
from strings import *
#lazy import tutorial
# lazy import functions
# lazy import strings

# from setuptools import setup
# from Cython.Build import cythonize

from random import randint, shuffle
#from enum import Enum

turnCount = 1
dragalterModifier = [0,0]
gameEnded = False
silverLining = False
panguardian = False
muscipulaRex = False
nobleShamanUsed = False
canModify = False
globalModifier = 0

activePlayer = activePlayerClass(2)

#Separate from the GUI, handles the main game once you enter a game with another player
def startGame(test="") -> None:
    if testingPhase:
        print("\n________________________________________________________________________________________________________________________________________________________________________________________________________________")
        print("PreGame Phase started\n")
    if testingPhase:
        print("\nMonster Deck:")
    shuffle(monsterDeck)
    drawMonsterCard(3)
    if ranked:
        shuffle(p1Deck)
        shuffle(p2Deck)
        #Start the first player's turn, determine who goes first
        #For ranked, run a coin flip. For all other modes, every player rolls the dice and highest roller goes first, then in clockwise.
        if not flipCoin(): activePlayer.increment()
    else:      
        #activePlayer.updatePlayerCount(4)
        shuffle(mainDeck)
        if testingPhase:
            print(f"Main Deck:  {mainDeck}")
        chooseLeader()
    for player in range(1,activePlayer.count()+1,1):
        drawCard(5,player)
    if testingPhase:
        print("PreGame Phase finished")
        print("\n________________________________________________________________________________________________________________________________________________________________________________________________________________")
        if test == "atk":
            playerHeroes[1] = ["Bad Axe","Meowzio", "Lucky Bucky"]
            monsterField[0] = "Abyss Queen"
            monsterField[1] = "Anuran Cauldron"
            monsterField[2] = "Bloodwing"
            if bool(input("Should win?")):
                playerMonsters[0].append("Ancient Megashark")
                playerMonsters[0].append("Reptilian Ripper")
            global heroItems
            heroItems[1] = ["","",""]
    main(test)
    return

#Is the main game loop. When the game ends, it returns to startGame which then ends
def main(test: str) -> None:
    while not gameEnded:
        global turnCount, heroAbilityUsed
        #Start of Turn
        if testingPhase:
            print(f"Player {activePlayer.current()} turn started")
        heroAbilityUsed = []
        for i in range(0,len(playerHeroes[activePlayer.current()])):
            heroAbilityUsed.append(False)
        startTurn() 
        chooseAction() #Basically, it waits for input
        if not test == "": #For efficiency while testing
            #have a match case/elif chain for the tests
            if test == "testWin Class":
                getPartyCounts(1)

        #End of Turn
        if testingPhase:
            print(f"Player {activePlayer.current()} End Phase started")
        if str(input()) == "end":
            endGame("Test",1)
        if not playerHand[activePlayer.current()]:
            if "Clawed Nightmare" in playerMonsters[activePlayer.current()]:
                first = int(input())
                second = int(input())
                pullCard(first)
                pullCard(second)
            if "Goretelodont" in playerMonsters[activePlayer.current()]:
                if askPlayer():
                    drawCard(3)
            if "Scavenger Griffin" in playerMonsters[activePlayer.current()]:
                stealHero()
        global silverLining, panguardian, nobleShamanUsed, globalModifier, canModify
        silverLining = panguardian = nobleShamanUsed = canModify = False
        globalModifier = 0
        playerEffects[activePlayer.current()] = []
        activePlayer.increment()
        turnCount += 1
        #All of this code (in the End of Turn section) MUST NOT cause anything to happen visually. It must run quickly before the game ends (if it does)
        #repeats while there is no winner
    return

#All the "Standby Phase" Stuff
def startTurn() -> None:
    global leaderAbilityUsed, heroAbilityUsed, AP
    leaderAbilityUsed = False
    AP = 3
    if "Mega Slime" in playerMonsters[activePlayer.current()]: AP += 1
    if testingPhase:
        print("Turn Number:", turnCount)
        #if turnCount > 1:
            #print(f"Start of turn effect: {playerLeaders[activePlayer.current()]["Start of Turn"]}")
    if (Leaders[playerLeaders[activePlayer.current()]]["Start of Turn"] and turnCount != 0): #Only for the KickStarter leaders and Individual Exclusive leaders
        leaderTypeSwitch()
        if testingPhase:
            print(f"{playerLeaders[activePlayer.current()]}: {leaderCurrentType[activePlayer.current()]}")
    heroAbilityUsed = []
    for hero in range(0,len(playerHeroes[activePlayer.current()])): #setup stuff, to make it easier
        if len(heroAbilityUsed) <= hero: heroAbilityUsed.append(False)
        else: heroAbilityUsed[hero] = False
    return

def chooseLeader() -> None: #Pick your leader at the start of the game. Only used in casual
    if testingPhase:
        print("     Leader Section:\n")
    for i in range(1, activePlayer.count()+1,1):
        leaderCurrentType[i] = Leaders[(playerLeaders[i])]["Class"]
        if testingPhase:
            print(f"Player {i}: {playerLeaders[i]}, Class: {leaderCurrentType[i]}")
    return

#For the KSE/IE leaders, asks player if they want to switch types, then switches if they say yes
def leaderTypeSwitch(leader=playerLeaders[activePlayer.current()]) -> None:
    if input(f"{switchLeaderType}\n") == "y":
        leaderType = leaderCurrentType[activePlayer.current()]
        match leader:
            case "Brutal Bow":
                #Fighter/Ranger
                if leaderType == heroClass.Fighter:
                    leaderCurrentType[activePlayer.current()] = heroClass.Ranger
                else:
                    leaderCurrentType[activePlayer.current()] = heroClass.Fighter
                return
            case "Mystical Maestro":
                #Wizard/Bard
                if leaderType == heroClass.Wizard:
                    leaderCurrentType[activePlayer.current()] = heroClass.Bard
                else:
                    leaderCurrentType[activePlayer.current()] = heroClass.Wizard
                return
            case "Veiled Raider":
                #Guardian/Thief
                if leaderType == heroClass.Guardian:
                    leaderCurrentType[activePlayer.current()] = heroClass.Thief
                else:
                    leaderCurrentType[activePlayer.current()] = heroClass.Guardian
                return
            case "Unstable Unicorn":
                #Copy another Leader
                if activePlayer.count() == 2:
                    if activePlayer.current() == 1:
                        unstableUnicornTarget[activePlayer.current()] = 2
                    else:
                        unstableUnicornTarget[activePlayer.current()] = 1
                else:
                    unstableUnicornTarget[activePlayer.current()] = choosePlayer()
                return
            case "Fierce Panguardian":
                #Guardian/Fighter
                if leaderType == heroClass.Guardian:
                    leaderCurrentType[activePlayer.current()] = heroClass.Fighter
                else:
                    leaderCurrentType[activePlayer.current()] = heroClass.Guardian
                return
            case "Illusive Trickster":
                #Wizard/Thief
                if leaderType == heroClass.Wizard:
                    leaderCurrentType[activePlayer.current()] = heroClass.Thief
                else:
                    leaderCurrentType[activePlayer.current()] = heroClass.Wizard
                return
            case "Rhythmic Archer":
                #Bard/Ranger
                if leaderType == heroClass.Bard:
                    leaderCurrentType[activePlayer.current()] = heroClass.Ranger
                else:
                    leaderCurrentType[activePlayer.current()] = heroClass.Bard
                return
    return

def flipCoin(count: int = 1, stopOnTails: bool = False) -> int:
    #0 = Tails, 1 = Heads
    return randint(0,1)

    #headCount = 0
    # if not stopOnTails and count == 1:
    #     return randint(0,1)
    # else:
    #     while tails == False:
    #         coinFlip = randint(0,1)
    #         if coinFlip == 0: tails = True
    #         headCount += coinFlip
    #return headCount

def rollDice(heroRoll: bool = False, index: int = 0, player: int = activePlayer.current()) -> int:
    diceRoll = randint(1,6) + randint(1,6)
    if player == activePlayer.current():
        diceRoll += globalModifier
    diceRoll += "Anuran Cauldron" in playerMonsters[player]
    if not heroRoll: return diceRoll
    if "Majestelk" in playerEffects[player]:
        response = int(input())
        match(response):
            case 0:
                diceRoll -= 5
            case 1:
                diceRoll += 5
            case _:
                diceRoll += 0
    #Items
    if heroItems[player][index] != "":
        equippedItem = heroItems[player][index]
        diceRoll += 2*(equippedItem == "Really Big Ring")
        diceRoll += 4*(equippedItem == "Even Bigger Ring")
        diceRoll -= 2*(equippedItem == "Curse of the Snake's Eyes")
        diceRoll += 2*silverLining
        if equippedItem == "Biggest Ring Ever":
            for i in range(0,3):
                index = selectFromHand(cardType.Any,player,canCancel=True)
                if index == -1:
                    continue
                discardSelected(index,player)
                diceRoll += 2
        elif equippedItem == "Mysterious Feather":
            index = selectFromHand(cardType.Any,player,canCancel=True)
            if index != -1:
                discardSelected(index,player)
                diceRoll += 3

    #Monsters
    diceRoll += "Dark Dragon King" in playerMonsters[player]

    #Leaders
    leaderEffect = playerLeaders[player]
    if leaderEffect == "Unstable Unicorn":
        leaderEffect = unstableUnicornTarget[player]
    global nobleShamanUsed

    match(leaderEffect):
        case "Charismatic Song":
            diceRoll += 1
        case "Piercing Howl":
            diceRoll += len(heroItems[player])
        case "Fearless Flame":
            if askPlayer():
                discardSpecific()
                diceRoll += 1
        
    for i in range(1,activePlayer.count()+1):
        if playerLeaders[i] == "Noble Shaman" and not nobleShamanUsed:
            if askPlayer():
                diceRoll -= 1
                nobleShamanUsed = True
    if testingPhase: print(f"Rolled: {diceRoll}")
    return diceRoll

def rollDie() -> int:
    return randint(1,6)

def chooseAction() -> None:
    global AP
    print(f"Active Player: {activePlayer.current()}")
    while AP > 0 and not gameEnded:
        print(playerHand[activePlayer.current()])
        action: str = input("Do:")
        match(action):
            case "end":
                AP = 0
                return
            case "draw":
                draw()
            case "redraw":
                discardDraw()
            case "atk":
                attack()
            case "hero":
                index: int = int(input())+1
                playHero(index,activePlayer.current())
            case "leader":
                activateLeaderAbility()
            case "play":
                index: int = int(input())+1
                playFromHand(index, Cards[playerHand[index]]["Card Type"])
            case "dt":
                index: int = int(input())+1
                print(Cards[playerHand[activePlayer.current()][index]]["Description"])
            case "field":
                print(f"Heroes: {playerHeroes[activePlayer.current()]}")
                print(f"Items: {heroItems[activePlayer.current()]}")
            case "gy":
                print(discardPile)
            case "monster":
                print(monsterField)
            case "stop":
                gameEnded = True
                return
    return

def playFromHand(card: int, cardType) -> None:
    if cardType == cardType.Hero:
        playHero(card)
    elif cardType == cardType.Magic:
        target = int(input(targetStr))
        playMagic(card,target)
    elif cardType == cardType.Item:
        target = int(input(targetStr))
        index = int(input())
        playItem(index, playerHand[activePlayer.current()][card],target)
    if testingPhase:
        print(playerHand[activePlayer.current()])
    return

def activateHeroAbility(index: int, summoned: bool = False, player: int = activePlayer.current()) -> None:
    global AP, silverLining, panguardian, heroAbilityUsed
    if heroAbilityUsed[index] and not heroItems[player][index] == "Bottomless Bag":
        if testingPhase:
            print("Ability already activated this turn")
        return
    if heroItems[player][index] == "Sealing Key":
        return
    if (AP < 1 or (AP < 2 and heroItems[player][index] == "Soulbound Grimoire")) and not summoned:
        print("No AP")
        return
    if not summoned:
        if heroItems[player][index] == "Soulbound Grimoire":
            reduceAP()
        reduceAP()
    diceRoll = rollDice(True,index,player) #includes item buffs
    index = len(playerHeroes[activePlayer.current()])-1
    #card = playerHeroes[activePlayer.current()][index]
    #print(f"Required: {Cards[card]["Effect Roll"]}")
    if not panguardian:
        diceRoll += modifier()
    if heroItems[player][index] == "Goblet of Caffeination" and diceRoll < Cards[playerHeroes[player][index]]["Effect Roll"]: 
        if askPlayer():
            discardPile.append(heroItems[player][index])
            heroItems[player][index] = ""
            diceRoll = rollDice(True,index,player)
            if not panguardian:
                diceRoll += modifier()
    if diceRoll >= Cards[playerHeroes[player][index]]["Effect Roll"]:
        heroAbilityUsed[index] = True
        #Leaders
        if playerLeaders[player] == "Veiled Raider" and diceRoll >= 12:
            stealHero()
        #Monsters
        if "Arctic Aries" in playerMonsters[player]:
            drawCard(player=player)
        #Items
        if heroItems[player][index] == "Suspiciously Shiny Coin":
            discardSpecific()
        useHeroAbility(playerHeroes[player][index])
    elif heroItems[player][index] != "": #If it has an item, run the item checks
        #Items
        if heroItems[player][index] == "Particularly Rusty Coin":
            drawCard(1)
        elif heroItems[player][index] == "Temporal Hourglass":
            AP += 1
        elif heroItems[player][index] == "Silver Lining":
            silverLining = True
        elif heroItems[player][index] == "Dragon's Bile":
            sacrifice(target=player)
    #Leaders
    if playerLeaders[player] == "Mystical Maestro" and diceRoll <= 4:
        drawCard(player=player)
    if "Reef Ripper" in playerMonsters[player] and diceRoll < Cards[playerHeroes[player][index]]["Effect Roll"]:
        drawCard(player=player)
    #TODO Here to Sleigh: Freshly Sharpened Skates / Milk and Cookies
    return

def activateLeaderAbility(leader=playerLeaders[activePlayer.current()]) -> None:
    global leaderAbilityUsed
    #Sets the Unicorn's ability to whatever it copied at the start of the turn
    if leader == "Unstable Unicorn":
        leader = playerLeaders[(unstableUnicornTarget[activePlayer.current()])]

    #Checks if it can be activated, pulls index of target leader so UU works
    if AP < Leaders[leader]["AP Cost"]:
        print("No AP left")
        return
    if not Leaders[leader]["Activatable"] or leaderAbilityUsed:
        print("Unable to use ability")
        return
    else:
        match leader:
            case "Shadow Claw":
                target = choosePlayer(1)
                #Need to get a target in the hand. will do rand for now
                pullCard(target, cardType.Any, 0)
                reduceAP()
                leaderAbilityUsed = True
                return
            case "Gnawing Dread":
                index = searchDiscard(cardType.Any)
                reduceAP(2)
                playerHand[activePlayer.current()].append(discardPile.pop(index))
                leaderAbilityUsed = True
                return
            case "Illusive Trickster":
                if checkHand(cardType.Magic, activePlayer.current()):
                    discardSpecific(cardType.Magic,1)
                    drawCard(3)
                    leaderAbilityUsed = True
                return
    return

def useHeroAbility(hero,player: int = activePlayer.current()) -> None:
    global playerEffects, globalModifier, AP, canModify, dragalterModifier
    match Cards[hero]["Effect"]:
        case cardEffect.BadAxe:
            index = chooseHero()
            target = choosePlayer()
            destroy(index, target, player)
        case cardEffect.PullCard:
            target = choosePlayer()
            if pullCard(target,cardType.Any,0):
                pullCard(target,cardType.Any,0)
        case cardEffect.BearyWise:
            allPlayersDiscard(hitSelf = False)
            addFromDiscard()
        case cardEffect.ForceDiscard:
            discardSpecific(count=2,target=choosePlayer(),canCancel=False)
        case cardEffect.PanChucks:
            drawCard(2)
            firstDraw = playerHand[activePlayer.current()][-2]
            secondDraw = playerHand[activePlayer.current()][-1]
            if testingPhase:
                print(f"Drew {firstDraw} and {secondDraw}")
            if Cards[firstDraw]["Effect"] == cardEffect.Challenge:
                revealCard(-2)
                destroy(chooseHero(),choosePlayer(),player)
            elif Cards[secondDraw]["Effect"] == cardEffect.Challenge:
                revealCard(-1)
                destroy(chooseHero(),choosePlayer(),player)
        case cardEffect.QiBear:
            count = int(input())
            for i in range(0,count):
                count = discardSpecific(canCancel=True)
            for i in range(0,count):
                destroy(chooseHero(),choosePlayer(),player)
            #discard up to 3, pop hero for each
        case cardEffect.ToughTeddy:
            #Every player owning a fighter discards
            hasFighter = False
            for player in range(1,activePlayer.count()+1):
                if player == activePlayer.current():
                    continue
                for j in range(0,len(playerHeroes[player])):
                    if Cards[playerHeroes[player][j]]["Class"] == heroClass.Fighter:
                        hasFighter = True
                        continue
                if hasFighter:
                    discardSpecific(target=player)
        case cardEffect.DodgyDealer:
            target = int(input(targetStr))
            tradeHands(targetTwo=target)
        case cardEffect.FuzzyCheeks:
            drawCard(1)
            playCards(type = cardType.Hero)
        case cardEffect.GreedyCheeks:
            return
        case cardEffect.LuckyBucky:
            if pullCard(choosePlayer(),cardType.Hero):
                if askPlayer():
                    playHero(-1,player,False)
        case cardEffect.MellowDee:
            drawCard()
            if Cards[playerHand[activePlayer.current()][-1]]["Card Type"] == cardType.Hero:
                if askPlayer():
                    playHero(-1,player,False)
        case cardEffect.TipsyTootie:
            index = int(input())
            selfIndex = int(input())
            trade(index, choosePlayer(), selfIndex)
        case cardEffect.CalmingVoice:
            playerEffects[activePlayer.current()].append("Calming Voice")
        case cardEffect.HolyCurselifter:
            index = int(input())
            playerHand[player].append(heroItems[player][index])
            heroItems[player][index] = ""
        case cardEffect.IronResolve:
            playerEffects[activePlayer.current()].append("Iron Resolve")
        case cardEffect.MightyBlade:
            playerEffects[activePlayer.current()].append("Mighty Blade")
        case cardEffect.VibrantGlow:
            globalModifier += 5
        case cardEffect.WiseShield:
            globalModifier += 3
        case cardEffect.Bullseye:
            return
        case cardEffect.Hook:
            playCards(player,1,cardType.Item)
            drawCard(player=player)
            return
        case cardEffect.QuickDraw:
            drawCard(2,player)
            indices = []
            if Cards[playerHand[player][-1]]["Card Type"] == cardType.Item:
                indices.append(-1)
            if Cards[playerHand[player][-2]]["Card Type"] == cardType.Item:
                indices.append(-2)
            finalIndex = int(input())
            playItem(finalIndex, playerHand[player][finalIndex],player)
            return
        case cardEffect.SeriousGrey:
            destroy(chooseHero(),choosePlayer(),player)
            drawCard(player=player)
        case cardEffect.SharpFox:
            target = choosePlayer()
            for i in range(0,len(playerHand[target])):
                print(playerHand[target][i]) #Reveal
        case cardEffect.Wildshot:
            drawCard(3,player)
            discardSpecific(count=1,target=choosePlayer())
        case cardEffect.WilyRed:
            count = 7 - len(playerHand[player])
            drawCard(count,player)
        case cardEffect.Meowzio:
            target = choosePlayer()
            pullCard(target)
            stealHero(playerTarget = target)
        case cardEffect.PlunderingPuma:
            target = choosePlayer()
            pullCard(target)
            pullCard(target)
            drawCard(player=target)
        case cardEffect.Shurikitty:
            destroy(chooseHero(),choosePlayer(),player, True)
        case cardEffect.SilentShadow:
            target = choosePlayer()
            for i in range(0,len(playerHand[target])):
                print(playerHand[target][i]) #Reveal
            index = int(input())
            playerHand[player].append(playerHand[target].pop(index))
        case cardEffect.SlipperyPaws:
            target = choosePlayer()
            pullCard(target)
            pullCard(target)
            discardSpecific(target=player)
        case cardEffect.SmoothMimimeow:
            for i in range(1,activePlayer.count()+1):
                if i == player:
                    continue
                if playerHand[i]: #Has 1+ cards in hand
                    for j in range(0,len(playerHeroes[i])):
                        if Cards[playerHeroes[i][j]]["Class"] == heroClass.Thief:
                            hasThief = True
                            continue
                    if hasThief:
                        pullCard(i)
        case cardEffect.BunBun:
            searchDiscard(cardType.Magic,player)
        case cardEffect.Fluffy:
            destroy(chooseHero(),chooseHero(),choosePlayer())
        case cardEffect.Hopper:
            sacrifice(choosePlayer())
        case cardEffect.Snowball:
            drawCard()
            if playerHand[activePlayer.current()][-1] == cardType.Magic:
                if askPlayer():
                    playMagic(-1,player)
                    drawCard()
        case cardEffect.Spooky:
            for i in range(1,activePlayer.count()+1):
                if i == player:
                    continue
                if playerHeroes[i]:
                    sacrifice(i)             
        case cardEffect.Whiskers:
            stealHero(player,choosePlayer())
            destroy(chooseHero(),chooseHero(),choosePlayer())
        case cardEffect.Wiggles:
            hasHero = False
            for i in range(1,activePlayer.count()+1):
                if len(playerHeroes[i]) > 0:
                    hasHero = True
                    continue
            if not hasHero: return
            stealHero(player,choosePlayer())
            activateHeroAbility(-1,player=player)
        case cardEffect.BigBuckley:
            attack(True)
        case cardEffect.BuckOmens:
            target = int(input())
            for i in range(0,len(playerHand[target])):
                print(playerHand[target][i])
            index = int(input())
            playerHand[player].append(playerHand[target].pop(index))
            playHero(-1,player,False)
        case cardEffect.DoeFallow:
            sacrifice(player)
            count = 7-len(playerHand[player])
            drawCard(count,player)
        case cardEffect.Maegisty:
            playerEffects[player].append("Maegisty")
        case cardEffect.MagusMoose:
            searchDiscard(cardType.Hero,player)
            if askPlayer():
                playHero(-1,player,False)
        case cardEffect.Majestelk:
            sacrifice(player)
            playerEffects[player].append("Majestelk")
        case cardEffect.Stagguard:
            playerEffects[player].append("Stagguard")
        case cardEffect.BlindingBlade:
            target = int(input())
            for i in range(0,len(heroItems[target])):
                playerHand[target].append(heroItems[target].pop(i))
        case cardEffect.CriticalFang:
            playerEffects[player].append("Critical Fang")
        case cardEffect.HardenedHunter:
            count = 0
            for i in range(1,activePlayer.count()+1):
                if i == player:
                    continue
                count += len(playerMonsters[i])
            drawCard(count,player)
        case cardEffect.LootingLupo:
            drawCard(len(heroItems[player]),player)
        case cardEffect.SilentShield:
            playerEffects[player].append("Silent Shield")
        case cardEffect.TenaciousTimber:
            for i in range(0,len(playerMonsters[player])):
                stealHero(player,int(input()))
        case cardEffect.WolfgangPack:
            globalModifier += len(playerHeroes[player]) - 1
        case cardEffect.Annihilator:
            searchDiscard(cardType.Challenge,player)
        case cardEffect.BrawlingSpirit:
            for i in range(1,activePlayer.count()+1):
                if len(playerHeroes[i]) > 2:
                    sacrifice(i)
        case cardEffect.GruesomeGladiator:
            for i in range(1,activePlayer.count()+1):
                if i == player:
                    continue
                pullCard(i,revealHand=True)
        case cardEffect.Meowntain:
            sacrifice(player)
            globalModifier += 5
        case cardEffect.RabidBeast:
            count = int(input())
            if count > len(playerHeroes[player]): count = len(playerHeroes[player])
            for i in range(0,count):
                sacrifice()
                destroy(chooseHero(),chooseHero(),choosePlayer())
        case cardEffect.RoaryalGuard:
            chosenClass = int(input())
            for i in range(1,activePlayer.count()+1):
                for j in range(0,len(playerHeroes[i])):
                    if Cards[playerHeroes[i][j]]["Class"] == chosenClass:
                        playerHand[i].append(playerHeroes[i].pop(j))
                        discardPile.append(heroItems[i].pop(j))
        case cardEffect.ViciousWildcat:
            index = int(input())
            playerMonsters[player].append(monsterField.pop(index))
            AP = 0
        case cardEffect.UnbridledFury:
            heroDestroyed = destroy(chooseHero(),choosePlayer(),player)
            if Cards[heroDestroyed]["Class"] == heroClass.Berserker:
                AP += 1
        case cardEffect.BarkHexer:
            allPlayersDiscard(True)
            allPlayersDiscard(False)
        case cardEffect.BeholdenRetriever:
            sacrifice(player)
            searchDiscard(cardType.Item,player,cardType.Hero)
        case cardEffect.BoneCollector:
            index = int(input())
            discardPile.append(heroItems[player].pop(index))
            searchDiscard(cardType.Hero,player)
            playHero(-1,player,False)
        case cardEffect.BostonTerror:
            target = choosePlayer()
            if bool(input()):
                pullCard(target)
            else:
                searchDiscard(player=player)
                searchDiscard(player=player)
        case cardEffect.GrimPupper:
            for i in range(1,activePlayer.count()+1):
                sacrifice(i)
        case cardEffect.HollowHusk:
            pullCard(choosePlayer(),cardType.Magic,True)
            if bool(input()):
                playMagic(-1,player)
        case cardEffect.PerfectVessel:
            index = playerHeroes[player].index("Perfect Vessel")
            discardPile.append(playerHeroes[player][index])
            stealHero(player,choosePlayer())
        case cardEffect.ShadowSaint:
            discardSpecific(cardType.Modifier,target=player)
            canModify = False
        case cardEffect.Dragalter:
            discardSpecific(cardType.Modifier)
            playerEffects[player].append("Dragalter")
            dragalterModifier = [Cards[discardPile[-1]]["Negative Effect"],Cards[discardPile[-1]]["Positive Effect"]]
        case cardEffect.Dystortivern:
            target = int(input())
            playerLeaders[player],playerLeaders[target] = playerLeaders[target],playerLeaders[player]
        case cardEffect.Extraga:
            for i in range(1,activePlayer.count()+1):
                for j in range(0,len(playerHeroes[i])):
                    if Cards[playerHeroes[i][j]]["Class"] == heroClass.Sorcerer:
                        playerHand[i].append(playerHeroes[i].pop(j))
                        discardPile.append(heroItems[i].pop(j))
        case cardEffect.Luut:
            target = choosePlayer()
            index = chooseHero(target)
            destination = chooseHero(player)
            heroItems[player][destination],heroItems[target][index] = heroItems[target][index],""
        case cardEffect.Mirroryu:
            index = int(input())
            useHeroAbility(playerHeroes[player][index])
        case cardEffect.Oracon:
            target = choosePlayer()
            if pullCard(target,cardType.Modifier):
                sacrifice(target)
        case cardEffect.Renovern:
            searchDiscard(cardType.Item,player)
            playItem(-1,playerHand[player][-1],player)
        case cardEffect.Shamanaga:
            searchDiscard(cardType.Hero,player)
            playHero(-1,player,False)
            sacrificeSpecific(player)
        case cardEffect.Smok:
            drawCard(2,player)
            if Cards[playerHand[player][-1]]["Card Type"] == cardType.Magic or Cards[playerHand[player][-2]]["Card Type"] == cardType.Magic:
                AP += 1
        case cardEffect.Bearserker:
            target = choosePlayer()
            discardHand(target)
            drawCard(3,target)
        case cardEffect.ComplexIllusion:
            drawCard(2,player)
            if Cards[playerHand[player][-1]]["Card Type"] == cardType.Modifier or Cards[playerHand[player][-2]]["Card Type"] == cardType.Modifier:
                AP += 1 #Reveal Card
        case cardEffect.Enchantler:
            count = int(input())
            if count > len(playerHand[player]): count = len(playerHand[player])
            discardSpecific(count=count,target=player)
            globalModifier += 2*count
        case cardEffect.Hamlet:
            for i in range(1,activePlayer.count()+1):
                for j in range(0,len(playerHeroes[i])):
                    if playerHeroes[i][j] == "Hamlet" and i == player:
                        continue
                    if Cards[playerHeroes[i][j]]["Class"] == heroClass.Bard:
                        playerHand[i].append(playerHeroes[i][j])
        case cardEffect.Hoodwink:
            target = choosePlayer()
            index = chooseHero()
            secondTarget = choosePlayer()
            secondIndex = chooseHero()
            heroItems[target][index],heroItems[secondTarget][secondIndex] = heroItems[secondTarget][secondIndex],heroItems[target][index]
        case cardEffect.PurringBandit:
            for i in range(1,activePlayer.count()+1):
                if i == player:
                    continue
                if len(playerHand[i]) > len(playerHand[player]):
                    pullCard(i)
        case cardEffect.NimbleGray:
            playerEffects[player].append("Nimble Gray")
        case cardEffect.Mimi:
            return
        case cardEffect.GiftBearer:
            return
        case cardEffect.SantaClaws:
            return
        case cardEffect.ChristmasCarol:
            return
        case cardEffect.LilDrummerBard:
            return
        case cardEffect.ShinyNose:
            return
        case cardEffect.SnowSlinger:
            return
        case cardEffect.Prancer:
            return
        case cardEffect.ShootingStar:
            return
        case cardEffect.FireplaceFugitive:
            return
        case cardEffect.GiftBagBandit:
            return
        case cardEffect.Evergreen:
            return
        case cardEffect.HollyJolly:
            return
        case cardEffect.Draw2: #Peanut
            drawCard(2)
        case cardEffect.SearchDiscard:
            searchDiscard(Cards[hero]["Search Target"])
        case cardEffect.StealHero:
            stealHero()
        case cardEffect.PullAndPlay:
            pullCard(choosePlayer(),True,Cards[hero]["Search Target"])
        case cardEffect.Play2:
            playCards(activePlayer.current(),2,type=Cards[hero]["Search Target"])
    return

def playCards(target = activePlayer.current(),count: int = 1,type=cardType.Any) -> None: #When you are forced to (aka given the option)
    index = int(input())
    for i in range(0,count):
        match(type):
            case cardType.Hero:
                playHero(index, target)
                return
            case cardType.Magic:
                playMagic(index, target)
                return
            case cardType.Item:
                return
    return

def playMagic(index,target: int = activePlayer.current()) -> None: #Play a magic card from your hand. Target is who it's used on
    global AP 
    discardPile.append(playerHand[target].pop(index))
    match(Cards[playerHand[target][index]]["Effect"]):
        case cardEffect.CallToTheFallen:
            searchDiscard(cardType.Hero)
        case cardEffect.CriticalBoost:
            drawCard(3)
            discardSpecific()
        case cardEffect.DestructiveSpell:
            discardSpecific()
            destroy(chooseHero(),chooseHero(),choosePlayer())
        case cardEffect.EnchantedSpell:
            global globalModifier
            globalModifier += 2
        case cardEffect.EntanglingTrap:
            discardSpecific(count=2)
            stealHero()
        case cardEffect.ForcedExchange:
            selfIndex = int(input())
            target = int(input(targetStr))
            trade(index,choosePlayer(),selfIndex)
            return
        case cardEffect.WindsOfChange:
            for i in range(1,activePlayer.count()+1):
                for i in range(0,len(heroItems[i])):
                    playerHand[i].append(heroItems[i].pop())
        case cardEffect.BeastCall:
            monsterDeck.insert(0,monsterField[0])
            monsterDeck.insert(0,monsterField[1])
            monsterDeck.insert(0,monsterField[2])
            monsterField[0] = monsterDeck.pop()
            monsterField[1] = monsterDeck.pop()
            monsterField[2] = monsterDeck.pop()
            AP += 1
        case cardEffect.RapidRefresh:
            discardHand()
            drawCard(4)
        case cardEffect.LightningLabrys:
            count = int(input())
            if count > len(playerHand[activePlayer.current()]):
                count = len(playerHand[activePlayer.current()])
            for i in range(0,count):
                discardSpecific()
                player = choosePlayer()
                sacrifice(player)
        case cardEffect.MassSacrifice:
            discardHand()
            drawCard(5)
        case cardEffect.EggOfFortune:
            discardSpecific()
            pullCard(choosePlayer())
        case cardEffect.CaptivatingSpell:
            globalModifier += 3
    if playerLeaders[target] == "Cloaked Sage":
        drawCard(player = target)
    if "Voltclaw Lion" in playerMonsters[target]:
        drawCard(player = target)
    return

def playItem(index, item, target:int = activePlayer.current()) -> None:
    if heroItems[target][index] != "":
        if testingPhase:
            print("An Item is already equipped")
        return
    if not "Warworn Owlbear" in playerMonsters[target]:
        if challenge(): 
            discardPile.append(playerHand[activePlayer.current()].pop(index))
            return
    heroItems[target][index] = item
    if item == "Morph Mask":
        roll = rollDie()
        match(roll):
            case 1:
                morphMaskType[target][index] = heroClass.Fighter
            case 2:
                morphMaskType[target][index] = heroClass.Ranger
            case 3:
                morphMaskType[target][index] = heroClass.Thief
            case 4:
                morphMaskType[target][index] = heroClass.Guardian
            case 5:
                morphMaskType[target][index] = heroClass.Bard
            case 6:
                morphMaskType[target][index] = heroClass.Wizard
    elif item == "Chaos Mask":
        roll = randint(1,6) + randint(1,6)
        match(roll):
            case 1 | 2 | 3:
                morphMaskType[target][index] = heroClass.Warrior
            case 4 | 5 | 6:
                morphMaskType[target][index] = heroClass.Druid
            case 7 | 8 | 9:
                morphMaskType[target][index] = heroClass.Berserker
            case 10 | 11 | 12:
                morphMaskType[target][index] = heroClass.Necromancer
    if "Wicked Sea Serpent" in playerMonsters[target]:
        drawCard(player=target)
    #Check if you won after equipping a class changing item
    if Cards[item]["Effect"] == cardEffect.Mask: getPartyCounts(target)
    return

def playHero(index,player=activePlayer.current(),loseAP: bool = True) -> None:
    if loseAP:
        reduceAP()
    if challenge(): return
    global heroAbilityUsed, heroItems
    heroAbilityUsed.append(False)
    if gamemode == 1 or (gamemode == 2 and len(playerHeroes[player]) < 5):
        playerHeroes[player].append(playerHand[player].pop(index))
    elif gamemode == 2 and len(playerHeroes[player]) == 5:
        tribute = int(input())
        playerHeroes[player][tribute] = playerHand[index]
        playerHand[player].pop(index)

    
    if len(heroItems[player]) < len(playerHeroes[player]): #Expands heroItems list to match the playerHeroes length
        heroItems[player].append("")
    if testingPhase: print(f"Items: {heroItems[player]}")
    activateHeroAbility(len(playerHeroes[player])-1,True,player)
    return

def trade(index: int, target: int, selfTarget: int) -> None:
    #Swap the heroes
    playerHeroes[target][index],playerHeroes[activePlayer.current()][selfTarget] = playerHeroes[activePlayer.current()][selfTarget],playerHeroes[target][index]
    #Swap the items
    heroItems[target][index],heroItems[activePlayer.current()][selfTarget] = heroItems[activePlayer.current()][selfTarget],heroItems[target][index]
    return

def askPlayer(output: str = "") -> bool: #A yes or no prompt
    if bool(input(output)): return True
    return False

def choosePlayer(req: str = "") -> int:
    if activePlayer.count() == 2: 
        player = not(activePlayer.current() - 1) + 1
        otherPlayer = player
    else:
        otherPlayer = int(input())
    match(req):
        case "hasCard": #has card in hand
            player = int(input())
            if not playerHand[activePlayer.current()] or (not playerHand[otherPlayer] and activePlayer.count() == 2):
                choosePlayer(req = "hasCard")   
        case "hasHero":
            player = int(input())
            if not playerHeroes[activePlayer.current()] or (not playerHeroes[otherPlayer] and activePlayer.count() == 2):
                choosePlayer(req = "hasHero")
        case "": #Non-specific, no requirements
            if activePlayer.count() == 2: 
                return player
            else:
                player = int(input())
    return player
    
def chooseHero(player=activePlayer.current()) -> int:
    index = int(input())
    return index

def challenge() -> bool:
    global panguardian
    player = 0
    if "Mighty Blade" in playerEffects[activePlayer.current()]:
        return
    hasChallenge = []
    for i in range(1,activePlayer.count()+1):
        if i != activePlayer.current() and hasCardEffect(cardEffect.Challenge,i):
                hasChallenge.append(i)
    for i in range(1,len(hasChallenge)+1):
        if askPlayer():
            discardSpecific(cardType.Challenge,1,i,False)
            player = i
            continue
    print(f"Player: {player}")
    if player == 0: return False #Breaks if no one challenges
    mainRoll = rollDice()
    if playerLeaders[activePlayer.current()] == "Fist of Reason":
        mainRoll += 2
    challengeRoll = rollDice()
    if playerLeaders[player] == "Fist of Reason":
        challengeRoll += 2
    if playerLeaders[player] == "Fierce Panguardian":
        panguardian = True
    if "Bloodwing" in playerMonsters[activePlayer.current()]:
        discardSpecific(target=player)
    mainRoll += "Titan Wyvern" in playerMonsters[activePlayer.current()]
    challengeRoll += "Titan Wyvern" in playerMonsters[player]
    mainRoll += modifier()
    challengeRoll += modifier() #TODO make this into one function call
    if "Possessed Plush" in playerMonsters[player]:
        drawCard(player=player)
    if mainRoll < challengeRoll:
        return False
    return True

def hasModifier() -> list[int]:
    hasChallenge:int = []
    stagguardPlayer = -1
    for i in range(1,activePlayer.count()+1):
        if "Stagguard" in playerEffects[i]:
            stagguardPlayer: int = i
    for j in range(1,activePlayer.count()+1):
        if not(stagguardPlayer == -1 or j == stagguardPlayer):
            continue
        for k in range(0,len(playerHand[j])):
            if Cards[playerHand[j][k]]["Card Type"] == cardType.Modifier:
                hasChallenge.append(j)
    return hasChallenge

def modifier(player: int = activePlayer.current()) -> int:
    count: int = 0
    netModifier = 0
    if not askAllToModifyOrChallenge:
        listPlayers: list[int] = hasModifier()
        for i in range(1,len(listPlayers)):
            if askPlayer(useModifier):
                netModifier += playModifier(listPlayers[i])
                count += 1
                if i != activePlayer.current() and "Abyss Queen" in playerMonsters[activePlayer.current()]:
                    netModifier += 1
    else:
        for i in range(1,activePlayer.count()+1):
            if askPlayer(output=useModifier):
                netModifier += playModifier(i)
                count += 1
                if i != activePlayer.current() and "Abyss Queen" in playerMonsters[activePlayer.current()]:
                    netModifier += 1
    if netModifier != 0:
        for i in range(1,activePlayer.count()+1):
            if "Crowned Serpent" in playerMonsters[i]:
                drawCard(player = i)
    for i in range(1,activePlayer.count()+1):
        if "Crowned Serpent" in playerMonsters[i]:
            drawCard(count,i)
    if "Dragalter" in playerEffects[player]:
        if bool(input()):
            netModifier += dragalterModifier[1]
        else:
            netModifier -= dragalterModifier[0]
    return netModifier

def playModifier(player) -> int:
    hasModifier = False
    boost = 0
    for i in range(0,len(playerHand[player])):
        if Cards[playerHand[player][i]]["Card Type"] == cardType.Modifier:
            hasModifier = True
    if not hasModifier:
        if testingPhase: print("You don't have a modifier")
        return 0
    index = int(input("Which Card: "))
    
    if Cards[playerHand[player][index]]["Positive Effect"] == 0:
        boost -= Cards[playerHand[player][index]]["Negative Effect"]
    elif Cards[playerHand[player][index]]["Negative Effect"] == 0:
        boost = Cards[playerHand[player][index]]["Positive Effect"]
    else:
        boostSign = int(input("+ or - (1 or 0): "))
        if boostSign == 1:
            boost = Cards[playerHand[player][index]]["Positive Effect"]
        else:
            boost -= Cards[playerHand[player][index]]["Negative Effect"]
    discardPile.append(playerHand[player].pop(index))
    if playerLeaders[player] == "Protecting Horn":
        bonus = int(input())
        match(bonus):
            case 0:
                boost += 1
            case 1:
                boost -= 1
            case _:
                return boost
    return boost

def hasCardEffect(effect,player=activePlayer.current()) -> bool:
    for i in range(0,len(playerHand[player])):
        if Cards[playerHand[player][i]]["Effect"] == effect:
            return True
    return False

def pullCard(target: int = activePlayer.current(),reqType: int = cardType.Any, revealHand: bool = False) -> bool:
    #target is who is stolen from, req is true/false for if there is a requirement, reqType is what card type you need to pull or else you dont pull
    index = -1
    if revealHand:
        for i in range(0,len(playerHand[target])):
            print(playerHand[target][i])
        index = int(input())
    else:
        shuffle(playerHand[target])
    pulledCard: str = playerHand[target].pop(index)
    if testingPhase:
        print(f"Pulled Card: {pulledCard}")
    playerHand[activePlayer.current()].append(pulledCard)
    return (Cards[pulledCard]["Card Type"] == reqType) #return if it matched the type you were looking for

def searchDiscard(cardType = cardType.Any, player: int = activePlayer.current(), alternateCardType = cardType.Any) -> None:
    return

def revealCard(index: int, player: int = activePlayer.current()) -> None:
    print(playerHand[player][index])
    return

def checkHand(cardType, player=activePlayer.current()) -> None:
    for card in playerHand[player]:
        if Cards[(playerHand[player][card])]["Card Type"] == cardType:
            return True
    return False

def handSize(player=activePlayer.current()) -> int:
    return len(playerHand[player])

def destroy(index,target,player: int = activePlayer.current(), shurikitty: bool = False) -> int: #target should be the index of the card
    #Always pops item, but only pops item if it has Decoy Doll
    global heroAbilityUsed
    heroDestroyed = 0
    if "Terratuga" in playerMonsters[target]: return heroDestroyed
    if not "Corrupted Sabretooth" in playerMonsters[player]:
        discardPile.append(heroItems[target].pop(index))
        if heroItems[target][index] != "Decoy Doll": #Protects the hero
            if "Maegisty" in playerEffects[player]:
                playerHand[player].append(playerHeroes[target].pop(index))
            else:
                heroDestroyed = playerHeroes[target][index]
                discardPile.append(playerHeroes[target].pop(index))
            heroAbilityUsed.pop(index)
        if playerLeaders[target] == "Brutal Bow":
            drawCard(1)
        for i in range(0,len(playerHeroes[target])):
            if heroItems[target][i] == "Soul Tether":
                if "Maegisty" in playerEffects[player]:
                    playerHand[player].append(playerHeroes[target].pop(i))
                else:
                    discardPile.append(playerHeroes[target].pop(i))
                if not shurikitty:
                    discardPile.append(heroItems[target].pop(i))
                else:
                    playerHand[player].append(heroItems[target].pop(i))
        if "Dracos" in playerMonsters[target]:
            drawCard(player = target)
        if "Wandering Behemoth" in playerMonsters[target]:
            drawCard(player = target)
    #else:
    return heroDestroyed

def sacrificeSpecific(target: int = activePlayer.current(),index: int = -1) -> None:
    hasHero = False #in hand
    if "Dragon Wasp" in playerMonsters[target]:
        if askPlayer():
            discardSpecific(count=2,target=target,canCancel=False)
            return
    if "Maegisty" in playerEffects[target]:
        playerHand[target].append(playerHeroes[target].pop(index))
        discardPile.append(heroItems[target].pop(index))
    else:
        discardPile.append(playerHeroes[target].pop(index))
        discardPile.append(heroItems[target].pop(index))
    for i in range(0,len(playerHeroes[target])):
        if heroItems[target][i] == "Soul Tether":
            if "Maegisty" in playerEffects[target]:
                playerHand[target].append(playerHeroes[target].pop(index))
            else:
                discardPile.append(playerHeroes[target].pop(index))
            discardPile.append(heroItems[target].pop(i))
            discardPile.append(heroItems[target].pop(index))
    if WarriorsAndDruids:
        for i in range(1,activePlayer.count()+1):
            if "Feral Dragon" in playerMonsters[i]:
                drawCard(player=i)
                continue
    if "Wandering Behemoth" in playerMonsters[target]:
        drawCard(player=target)
    if "Doombringer" in playerMonsters[target]:
        searchDiscard(cardType.Any,target)
    if "Saffyre Phoenix" in playerHand[target]:
        for i in range(0,len(playerHand[target])):
            if Cards[playerHand[target][i]]["Card Type"] == cardType.Hero:
                hasHero = True
                continue
        if hasHero:
            if askPlayer():
                index = int(input())
                playHero(index,target)
    return

def sacrifice(target: int = activePlayer.current(),heroClass=heroClass.NoClass, count: int = 1, forcedIndex: int = 0) -> None:
    global heroAbilityUsed
    hasHero = False #in hand
    if "Dragon Wasp" in playerMonsters[target]:
        if askPlayer():
            discardSpecific(count=2,target=target,canCancel=False)
            return
    for i in range(0,count):
        index = chooseHero(target)
        if "Maegisty" in playerEffects[target]:
            playerHand[target].append(playerHeroes[target].pop(index))
            discardPile.append(heroItems[target].pop(index))
        else:
            discardPile.append(playerHeroes[target].pop(index))
            discardPile.append(heroItems[target].pop(index))
        heroAbilityUsed.pop(index)
    for i in range(0,len(playerHeroes[target])):
        if heroItems[target][i] == "Soul Tether":
            if "Maegisty" in playerEffects[target]:
                playerHand[target].append(playerHeroes[target].pop(index))
            else:
                discardPile.append(playerHeroes[target].pop(index))
            discardPile.append(heroItems[target].pop(i))
            discardPile.append(heroItems[target].pop(index))
    if WarriorsAndDruids:
        for i in range(1,activePlayer.count()+1):
            if "Feral Dragon" in playerMonsters[i]:
                drawCard(player=i)
                continue
    if "Wandering Behemoth" in playerMonsters[target]:
        drawCard(player=target)
    if "Doombringer" in playerMonsters[target]:
        for i in range(0,count):
            searchDiscard(cardType.Any,target)
    if "Saffyre Phoenix" in playerHand[target]:
        for i in range(0,len(playerHand[target])):
            if Cards[playerHand[target][i]]["Card Type"] == cardType.Hero:
                hasHero = True
                continue
        if hasHero:
            if askPlayer():
                index = int(input())
                playHero(index,target)
    return

def stealHero(playerDestination: int = activePlayer.current(), playerTarget: int = activePlayer.current()) -> None:
    global heroAbilityUsed
    if activePlayer.count() == 2 and "Calming Voice" in playerEffects[not(activePlayer.current()-1)+1]:
        print("Cannot steal a hero from this player by Calming Voice's effect")
        return
    if playerTarget == activePlayer.current():
        playerTarget = choosePlayer()
        if "Calming Voice" in playerEffects[playerTarget]:
            stealHero(playerDestination,playerTarget)
    index = int(input())
    playerHeroes[playerDestination].append(playerHeroes[playerTarget].pop(index))
    heroItems[playerDestination].append(heroItems[playerTarget].pop(index))
    heroAbilityUsed.pop(index)
    if WarriorsAndDruids:
        for i in range(0,len(playerHeroes[playerTarget])):
            if heroItems[playerTarget][i] == "Cursed Glove":
                playerHeroes[playerDestination].append(playerHeroes[playerTarget].pop(i))
                heroItems[playerDestination].append(heroItems[playerTarget].pop(i))
    return

def tradeHands(targetOne: int = activePlayer.current(), targetTwo: int = not(activePlayer.current()-1)+1) -> None:
    playerHand[targetOne], playerHand[targetTwo] = playerHand[targetTwo], playerHand[targetOne]
    return

def allPlayersDiscard(hitSelf: bool = True, type=cardType.Any) -> None:
    for i in range(1,activePlayer.count()+1):
        if hitSelf or i != activePlayer.current():
            discardSpecific(type,1,i)
    return

def addFromDiscard(count: int = activePlayer.count()-1, player: int = activePlayer.current()) -> None:
    for i in range(count-1,-1,-1):
        print(discardPile[i])
    index = int(input())
    playerHand[player].append(discardPile.pop(-index))
    return

def draw() -> None: #Spend AP and draw a card as an action
    if not ("Muscipula Rex" in playerMonsters[activePlayer.current()] and not muscipulaRex):
        reduceAP()
    if not "Lumbering Demon" in playerMonsters[activePlayer.current()]:
        drawCard()
    else:
        if askPlayer():
            drawCard(2)
            discardSpecific()
        else:
            drawCard()
    return

def shuffleGYintoDeck() -> None:
    global mainDeck, discardPile
    mainDeck = discardPile
    discardPile = []
    shuffle(mainDeck)
    return

def drawCard(count: int = 1, player: int = activePlayer.current()) -> None:
    newCount = 0
    shuffle = False
    if len(mainDeck) < count:
        newCount = count - len(mainDeck)
        count = len(mainDeck)
        shuffle = True
    for i in range(0,count):
        playerHand[player].append(mainDeck.pop())
    discardIndex = []
    if testingPhase:
        print(f"Negative count: {-count}")
    for i in range(-1,-count-1,-1):
        print(f"Index: {i}")
        print(f"Card: {playerHand[player][i]}")
        if Cards[playerHand[player][i]]["Card Type"] == cardType.Modifier and "Rex Major" in playerMonsters[player]:
            if askPlayer("Draw Again?"):
                newCount += 1
        elif Cards[playerHand[player][i]]["Card Type"] == cardType.Challenge and "Calamity Mongrel" in playerMonsters[player]:
            if askPlayer("Discard and Draw 2 More?"):
                newCount += 2
                discardIndex.append(i)
                discardPile.append(playerHand[player].pop(i))
        elif Cards[playerHand[player][i]]["Card Type"] == cardType.Magic and "Orthus" in playerMonsters[player]:
            if askPlayer():
                playMagic(i,player)
        elif Cards[playerHand[player][i]]["Card Type"] == cardType.Item and "Malamammoth" in playerMonsters[player]:
            if askPlayer():
                index = int(input())
                playItem(index,playerHand[player][i],player)
    if testingPhase:
        print(f"newCount: {newCount}")
        print(playerHand[player])
    if shuffle:
        shuffleGYintoDeck()
    if discardIndex:
        for i in range(0,len(discardIndex)):
            discardPile.append(playerHand[player].pop(discardIndex))
    if newCount > 0:
        drawCard(newCount,player)
    return

def drawMonsterCard(count=1) -> None:
    for i in range(2,2-count,-1):
        monsterField[i] = monsterDeck[-1]
        monsterDeck.pop()
    if testingPhase:
        print(f"{count} Monster Card(s) were/was drawn")
        print(monsterField)
    return

def attack(dontLoseAP=False) -> None:
    if AP < 2 and not dontLoseAP:
        print("Not enough AP")
        return
    monster = selectMonster()
    if not checkAtkRequirements(monsterField[monster]) and not "Nimble Gray" in playerEffects[activePlayer.current()]:
        print("Doesn't meet Party Requirements")
        return
    if not dontLoseAP:
        reduceAP(2)
    diceRoll = rollDice()
    diceRoll += (playerLeaders[activePlayer.current()] == "Divine Arrow" or (playerLeaders[activePlayer.current()] == "Unstable Unicorn" and playerLeaders[unstableUnicornTarget[activePlayer.current()]] == "Divine Arrow"))
    if "Reptilian Ripper" in playerMonsters[activePlayer.current()]:
        diceRoll += 2
    if "Ancient Megashark" in playerMonsters[activePlayer.current()]:
        diceRoll += 1
    if "Critical Fang" in playerEffects[activePlayer.current()]:
        diceRoll += 4
    for player in range(1,activePlayer.count()+1): #Checks all player parties
        if player == activePlayer.current(): #Don't apply the negative to yourself
            continue
        if "Chitin Scourge" in playerMonsters[player]:
            diceRoll -= 1
    # if testingPhase:
    #     diceRoll = 12
    print(f"Rolled a: {diceRoll}")
    if diceRoll >= Monsters[monsterField[monster]]["Win Roll"]:
        effect = Monsters[monsterField[monster]]["Win Effect"]
    elif diceRoll <= Monsters[monsterField[monster]]["Lose Roll"]:
        effect = Monsters[monsterField[monster]]["Lose Effect"]
    else:
        effect = monsterRollEffect.noEffect
    if testingPhase:
        print(f"Effect: {effect}")
    if playerLeaders[activePlayer.current()] == "Rhythmic Archer" or (playerLeaders[activePlayer.current()] == "Unstable Unicorn" and playerLeaders[unstableUnicornTarget[activePlayer.current()]] == "Rhythmic Archer"):
        if effect != monsterRollEffect.slay:
            drawCard()
    
    match(effect):
        case monsterRollEffect.slay:
                if len(playerMonsters[activePlayer.current()-1]) < 2:
                    if playerLeaders[activePlayer.current()] == "Raging Manticore" or (playerLeaders[activePlayer.current()] == "Unstable Unicorn" and playerLeaders[unstableUnicornTarget[activePlayer.current()]] == "Raging Manticore"):
                        drawCard()
                    #Copy the card to the player's field and then replace it with one from the Deck
                    print(f"Monster attacked: {monsterField[monster]}")
                    playerMonsters[activePlayer.current()].append(monsterField[monster])
                    print(f"Player {activePlayer.current()}'s Monsters: {playerMonsters[activePlayer.current()]}")
                    if testingPhase:
                        print(f"{monsterField[monster]} was slain by Player {activePlayer.current()}")
                    monsterField[monster] = monsterDeck.pop()
                    if testingPhase:
                        print(f"Monsters: {monsterField}")
                    monsterField[monster] = monsterDeck.pop()
                    if playerLeaders[activePlayer.current()] == "Raging Manticore":
                        drawCard(2)
                    if testingPhase:
                        print(f"Monsters: {monsterField}")
                else:
                    endGame("Monsters",activePlayer.current())
        case monsterRollEffect.discard:
            discardSpecific()
        case monsterRollEffect.discardTwo:
            discardSpecific(count=2)
        case monsterRollEffect.discardHand:
            discardHand()
        case monsterRollEffect.sacrifice:
            sacrifice()
        case monsterRollEffect.sacrificeTwo:
            sacrifice(count=2)
        case _:
            return
    return

def endGame(typeOfWin: str, winningPlayer: int = activePlayer.current()) -> None:
    global gameEnded
    gameEnded = True
    if typeOfWin == "Classes":
        winType = winByClasses
    elif typeOfWin == "Monsters":
        winType = winByMonsters
    elif typeOfWin == "Test":
        winType = winByTest
    else: #Potentially unnecessary
        gameEnded = False
    print(f"Player {winningPlayer} won by {winType}.")
    return #Goes back to where you were, eventually returning to main, which ends the game loop

def selectMonster() -> int:
    index = int(input("Which Monster: ")) - 1
    if index < 0 or index > 2:
        selectMonster()
    return index

def checkAtkRequirements(monster) -> bool:
    heroCount, classSet = getPartyCounts()
    if heroCount < Monsters[monster]["Hero Req"]:
        if testingPhase:
            heroReq = Monsters[monster]["Hero Req"]
            print(f"Not enough Heroes: {heroCount} out of {heroReq}")
        return False
    if (Monsters[monster]["Class Req"] != heroClass.NoClass) and not (Monsters[monster]["Class Req"] in classSet):
        if testingPhase:
            classReq = Monsters[monster]["Class Req"]
            print(f"No Hero of class {classReq}")
        return False
    return True

def getPartyCounts(target: int = activePlayer.current()) -> tuple[int,list]: #Returns an int value and a list of enum'd ints
    if testingPhase:
        print("Getting class counts")
    heroCount = len(playerHeroes[target])
    classSet = set() #It's a set for no duplicates
    for card in range(0, heroCount):
        if testingPhase:
            print(f"Item: {heroItems[target][card]}")
        mask = heroItems[target][card]
        if Cards[mask]["Effect"] == cardEffect.Mask:
            if mask == "Morph Mask":
                classSet.add(morphMaskType[target][card])
            else:
                classSet.add(Cards[heroItems[target][card]]["Mask Type"])
        else:
            classSet.add(Cards[playerHeroes[target][card]]["Class"])
    classSet.add(leaderCurrentType[target])
    if testingPhase:
        print(f"Hero Count: {heroCount}")
        print(f"Classes in Party: {classSet}")
    if len(classSet) == 6:
        endGame("Classes", target)
    return heroCount, classSet

def discardHand(player=activePlayer.current()) -> None:
    if not playerHand[activePlayer.current()]: return #Return if empty
    handSize = len(playerHand[player])
    for card in range(0,handSize):
        discardPile.append(playerHand[player].pop())
    for i in range(1,activePlayer.count()+1):
        if "Razor Tongue" in playerMonsters[i]:
            drawCard(player=i)
    return

def discardDraw() -> None: #Pay 3 AP, discard your hand, draw 5
    if AP > 2:
        reduceAP(3)
    else:
        print("Not enough AP")
        return
    discardHand()
    drawCard(5)
    return

def discardSpecific(type=cardType.Any,count=1,target=activePlayer.current(), canCancel: bool = False) -> int:
    if not playerHand[target]: return
    if len(playerHand[target]) < count: count = len(playerHand[target])
    for i in range(0,count):
        cardIndex = selectFromHand(type,target, canCancel)
        if cardIndex == -1:
            count = i
            continue
        discardSelected(cardIndex,target)
    for i in range(1,activePlayer.count()+1):
        if "Razor Tongue" in playerMonsters[i] and i != target:
            drawCard(player=i)
    return count

def selectFromHand(type=cardType.Any,target=activePlayer.current(), canCancel: bool = False) -> int:
    cancelled = False #If the player wants to cancel
    index = int(input())-1
    if type != Cards[playerHand[target][index]]["Card Type"]:
        selectFromHand(type,target)
    elif cancelled and canCancel:
        return -1
    return index

def discardSelected(cardIndex,target=activePlayer.current()) -> None:
    discardPile.append(playerHand[target].pop(cardIndex))
    return

def reduceAP(APReduction: int = 1) -> None:
    global AP
    AP -= APReduction
    if testingPhase:
        print(f"AP: {AP}")
    return

#Stores the x and y values of a button, as when a button is hidden it loses said values
class position:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
