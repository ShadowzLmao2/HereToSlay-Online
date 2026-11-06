from config import *
from cards import *
from active_player import *
from tutorial import *
import sys
from functions import *
from strings import *
import random
#from enum import Enum
activePlayer = 1
turnCount = 1
playerCount = 2
dragalterModifier = [0,0]
gameEnded = False
silverLining = False
panguardian = False
muscipulaRex = False
nobleShamanUsed = False
canModify = False
globalModifier = 0

#Separate from the GUI, handles the main game once you enter a game with another player
def startGame(test="None") -> None:
    global playerCount, activePlayer
    if testingPhase:
        print("\n________________________________________________________________________________________________________________________________________________________________________________________________________________")
        print("PreGame Phase started\n")
    if testingPhase:
        print("\nMonster Deck:")
    random.shuffle(monsterDeck)
    drawMonsterCard(3)
    if ranked:
        random.shuffle(p1Deck)
        random.shuffle(p2Deck)
        playerCount = 2
        #Start the first player's turn, determine who goes first
        #For ranked, run a coin flip. For all other modes, every player rolls the dice and highest roller goes first, then in clockwise.
        activePlayer = flipCoin()+1
    else:        
        random.shuffle(mainDeck)
        if testingPhase:
            print(f"Main Deck:  {mainDeck}")
        chooseLeader()
    for player in range(1,playerCount+1,1):
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
            heroItems[1] = ["None","None","None"]
    main(test)
    return

#Is the main game loop. When the game ends, it returns to startGame which then ends
def main(test: str) -> None:
    while not gameEnded:
        global activePlayer, playerCount, turnCount
        #Start of Turn
        if testingPhase:
            print(f"Player {activePlayer} turn started")
        startTurn() 
        chooseAction() #Basically, it waits for input
        if not test == "None": #For efficiency while testing
            #have a match case/elif chain for the tests
            if test == "testWin Class":
                getPartyCounts(1)

        #End of Turn
        if testingPhase:
            print(f"Player {activePlayer} End Phase started")
        if str(input()) == "end":
            endGame("Test")
        if not playerHand[activePlayer]:
            if "Clawed Nightmare" in playerMonsters[activePlayer]:
                first = int(input())
                second = int(input())
                pullCard(first)
                pullCard(second)
            if "Gorteledont" in playerMonsters[activePlayer]:
                if askPlayer():
                    drawCard(3)
            if "Scavenger Griffin" in playerMonsters[activePlayer]:
                stealHero()
        global silverLining, panguardian, nobleShamanUsed, globalModifier, canModify
        silverLining, panguardian, nobleShamanUsed, canModify = False
        globalModifier = 0
        playerEffects[activePlayer] = []
        if activePlayer == playerCount:
            activePlayer = 1
        else:
            activePlayer +=1
        turnCount +=1
        #All of this code (in the End of Turn section) MUST NOT cause anything to happen visually. It must run quickly before the game ends (if it does)
        #repeats while there is no winner
    return

#All the "Standby Phase" Stuff
def startTurn(player=activePlayer) -> None:
    global leaderAbilityUsed, activatedHeroAbility, AP
    leaderAbilityUsed = False
    AP = 3
    if "Mega Slime" in playerMonsters[activePlayer]: AP += 1
    if testingPhase:
        print("Turn Number:", turnCount)
        #if turnCount > 1:
            #print(f"Start of turn effect: {playerLeaders[activePlayer]["Start of Turn"]}")
    if (Leaders[playerLeaders[activePlayer]]["Start of Turn"] and turnCount != 0): #Only for the KickStarter leaders and Individual Exclusive leaders
        leaderTypeSwitch()
        if testingPhase:
            print(f"{playerLeaders[activePlayer]}: {leaderCurrentType[activePlayer]}")
    activatedHeroAbility = []
    for hero in range(0,len(playerHeroes[activePlayer])): #setup stuff, to make it easier
        if len(activatedHeroAbility) <= hero: activatedHeroAbility.append(False)
        else: activatedHeroAbility[hero] = False
    return

def chooseLeader() -> None: #Pick your leader at the start of the game. Only used in casual
    if testingPhase:
        print("     Leader Section:\n")
    for i in range(1, playerCount+1,1):
        leaderCurrentType[i] = Leaders[(playerLeaders[i])]["Class"]
        if testingPhase:
            print(f"Player {i}: {playerLeaders[i]}, Class: {leaderCurrentType[i]}")
    return

#For the KSE/IE leaders, asks player if they want to switch types, then switches if they say yes
def leaderTypeSwitch(leader=playerLeaders[activePlayer]) -> None:
    if input(f"{switchLeaderType}\n") == "y":
        leaderType = leaderCurrentType[activePlayer]
        match leader:
            case "Brutal Bow":
                #Fighter/Ranger
                if leaderType == heroType.Fighter:
                    leaderCurrentType[activePlayer] = heroType.Ranger
                else:
                    leaderCurrentType[activePlayer] = heroType.Fighter
                return
            case "Mystical Maestro":
                #Wizard/Bard
                if leaderType == heroType.Wizard:
                    leaderCurrentType[activePlayer] = heroType.Bard
                else:
                    leaderCurrentType[activePlayer] = heroType.Wizard
                return
            case "Veiled Raider":
                #Guardian/Thief
                if leaderType == heroType.Guardian:
                    leaderCurrentType[activePlayer] = heroType.Thief
                else:
                    leaderCurrentType[activePlayer] = heroType.Guardian
                return
            case "Unstable Unicorn":
                #Copy another Leader
                if playerCount == 2:
                    if activePlayer == 1:
                        unstableUnicornTarget[activePlayer] = 2
                    else:
                        unstableUnicornTarget[activePlayer] = 1
                else:
                    unstableUnicornTarget[activePlayer] = choosePlayer()
                return
            case "Fierce Panguardian":
                #Guardian/Fighter
                if leaderType == heroType.Guardian:
                    leaderCurrentType[activePlayer] = heroType.Fighter
                else:
                    leaderCurrentType[activePlayer] = heroType.Guardian
                return
            case "Illusive Trickster":
                #Wizard/Thief
                if leaderType == heroType.Wizard:
                    leaderCurrentType[activePlayer] = heroType.Thief
                else:
                    leaderCurrentType[activePlayer] = heroType.Wizard
                return
            case "Rhythmic Archer":
                #Bard/Ranger
                if leaderType == heroType.Bard:
                    leaderCurrentType[activePlayer] = heroType.Ranger
                else:
                    leaderCurrentType[activePlayer] = heroType.Bard
                return
    return

def flipCoin(count: int = 1, stopOnTails: bool = False) -> int:
    #0 = Tails, 1 = Heads
    for i in range(0,count):
        coinFlip = random.int(0,1)
        #if not coinFlip and stopOnTails:
            #continue
    return coinFlip

def rollDice(heroRoll: bool = False, index: int = 0, player: int = activePlayer) -> int:
    diceRoll = random.randint(1,6) + random.randint(1,6)
    if player == activePlayer:
        diceRoll += globalModifier
    diceRoll += "Anuran Cauldron" in playerMonsters[player]
    if not heroRoll: return diceRoll
    if "Majestelk" in playerEffects(player):
        response = int(input())
        match(response):
            case 0:
                diceRoll -= 5
            case 1:
                diceRoll += 5
            case _:
                diceRoll += 0
    #Items
    if heroItems[player][index] != "None":
        diceRoll += 2*(heroItems[player][index] == "Really Big Ring")
        diceRoll += 4*(heroItems[player][index] == "Even Bigger Ring")
        diceRoll += 2*silverLining
        diceRoll -= 2*(heroItems[player][index] == "Cursed of the Snake's Eyes")
        if heroItems[player][index] == "Biggest Ring Ever":
            for i in range(0,3):
                index = selectFromHand(cardType.Any,player,canCancel=True)
                if index == -1:
                    continue
                discardSelected(index,player)
                diceRoll += 2
        elif heroItems[player][index] == "Mysterious Feather":
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
        
    for i in range(0,playerCount):
        if playerLeaders[i] == "Noble Shaman" and not nobleShamanUsed:
            if askPlayer():
                diceRoll -= 1
                nobleShamanUsed = True
    return diceRoll

def rollDie() -> int:
    return random.randint(1,6)

def chooseAction() -> None:
    global AP
    while AP > 0 and not gameEnded:
        action: str = input("Do:")
        match(action):
            case "End":
                AP = 0
                return
            case "Draw":
                draw()
            case "Redraw":
                discardDraw()
            case "atk":
                attack()
            case "Hero":
                index: int = int(input())
                activateHeroAbility(playerHeroes[index],index)
            case "Leader":
                activateLeaderAbility()
            case "Play":
                index: int = int(input())
                playFromHand(index, Cards[playerHand[index]]["Card Type"])


    #Working: draw() discardDraw() attack() playFromHand()
    #WIP: activateHeroAbility(hero) activateLeaderAbility(leader) playMagic()
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
        playItem(index, playerHand[activePlayer][card],target)
    if testingPhase:
        print(playerHand[activePlayer])
    return

def activateHeroAbility(index: int, summoned: bool = False, player: int = activePlayer) -> None:
    global AP, silverLining, panguardian
    if activatedHeroAbility[index] and not heroItems[player][index] == "Bottomless Bag":
        if testingPhase:
            print("Ability already activated this turn")
        return
    if heroItems[player][index] == "Sealing Key":
        return
    if (AP < 0 or (AP < 1 and heroItems[player][index] == "Soulbound Grimoire")) and not summoned:
        print("No AP")
        return
    if not summoned:
        if heroItems[player][index] == "Soulbound Grimoire":
            reduceAP()
        reduceAP()
    diceRoll = rollDice(True,index,player) #includes item buffs
    if not panguardian:
        diceRoll += modifier()
    if heroItems[player][index] == "Goblet of Caffeination" and diceRoll < Cards[playerHeroes[player][index]]["Effect Roll"]: 
        if askPlayer():
            discardPile.append(heroItems[player][index])
            heroItems[player][index] = "None"
            diceRoll = rollDice()
            if not panguardian:
                diceRoll += modifier()
    if diceRoll >= Cards[playerHeroes[player][index]]["Effect Roll"]:
        activatedHeroAbility[index] = True
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
    elif heroItems[player][index] != "None":
        #Leaders
        if playerLeaders[player] == "Mystical Maestro" and diceRoll <= 4:
            drawCard()
        #Items
        if heroItems[player][index] == "Particularly Rusty Coin":
            drawCard(1)
        elif heroItems[player][index] == "Temporal Hourglass":
            AP += 1
        elif heroItems[player][index] == "Silver Lining":
            silverLining = True
        elif heroItems[player][index] == "Dragon's Bile":
            sacrifice(target=player)
    if "Reef Ripper" in playerMonsters[player] and diceRoll < Cards[playerHeroes[player][index]]["Effect Roll"]:
        drawCard(player=player)
    #TODO Here to Sleigh: Freshly Sharpened Skates / Milk and Cookies
    return

#Used for useLeaderAbility
leaderAbilityUsed= False

def activateLeaderAbility(leader=playerLeaders[activePlayer]) -> None:
    #global leaderAbilityUsed
    #Sets the Unicorn's ability to whatever it copied at the start of the turn
    if leader == "Unstable Unicorn":
        leader = playerLeaders[(unstableUnicornTarget[activePlayer])]

    #Checks if it can be activated, pulls index of target leader so UU works
    if AP < Leaders[leader]["AP Cost"]:
        print("No AP left")
        return
    if not Leaders[leader]["Activatable"] or leaderAbilityUsed:
        print("Unable to use ability")
        return
    else:
        match Leaders[leader]:
            case "Shadow Claw":
                target = choosePlayer(1)
                #Need to get a target in the hand. will do rand for now
                pullCard(target, False, 0)
                reduceAP()
                leaderAbilityUsed = True
                return
            case "Gnawing Dread":
                index = searchDiscard(cardType.Any)
                reduceAP(2)
                playerHand[activePlayer].append(discardPile[index].pop())
                leaderAbilityUsed = True
                return
            case "Illusive Trickster":
                if checkHand(cardType.Magic, activePlayer):
                    discardSpecific(cardType.Magic,1)
                    drawCard(3)
                    leaderAbilityUsed = True
                return
    return

def useHeroAbility(hero) -> None:
    global playerEffects, globalModifier, AP, canModify, dragalterModifier
    match Cards[hero]["Effect"]:
        case cardEffect.BadAxe:
            player = choosePlayer()
            target = chooseHero()
            destroy(target, player)
        case cardEffect.PullCard:
            target = choosePlayer()
            pulledCard = pullCard(target,False,0)
            if Cards[pulledCard]["Class"] == Cards[hero]["Pull Type"]:
                pullCard(target,False,0)
        case cardEffect.BearyWise:
            allPlayersDiscard(hitSelf = False)
            addFromDiscard()
        case cardEffect.ForceDiscard:
            discardSpecific(choosePlayer(),2,1)
        case cardEffect.PanChucks:
            drawCard(2)
            firstDraw = playerHand[activePlayer][-2]
            secondDraw = playerHand[activePlayer][-1]
            if testingPhase:
                print(f"Drew {firstDraw} and {secondDraw}")
                if Cards[activePlayer][firstDraw]["Effect"] == cardEffect.Challenge:
                    revealCard(-2)
                    player = choosePlayer()
                    target = chooseHero()
                    destroy(target, player)
                elif Cards[activePlayer][secondDraw]["Effect"] == cardEffect.Challenge:
                    revealCard(-1)
                    player = choosePlayer()
                    target = chooseHero()
                    destroy(target, player)
        case cardEffect.QiBear:
            count = int(input())
            for i in range(0,count):
                count = discardSpecific(canCancel=True)
            for i in range(0,count):
                index = int(input())
                player = choosePlayer()
                destroy()
            #discard up to 3, pop hero for each
        case cardEffect.ToughTeddy:
            #Every player owning a fighter discards
            for player in range(1,playerCount,1):
                if player == activePlayer:
                    continue
                for j in playerHeroes[player]:
                    if Cards[playerHeroes[player][j]]["Class"] == heroType.Fighter:
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
                    playHero(playerHand[player][-1],player,False)
        case cardEffect.MellowDee:
            drawCard()
            if playerHand[activePlayer][-1] == cardType.Hero:
                if askPlayer():
                    playHero(playerHand[player][-1],player,False)
        case cardEffect.TipsyTootie:
            index = int(input())
            selfIndex = int(input())
            trade(index, choosePlayer(), selfIndex)
        case cardEffect.CalmingVoice:
            playerEffects[activePlayer].append("Calming Voice")
        case cardEffect.HolyCurselifter:
            index = int(input())
            playerHand.append(heroItems[player][index])
            heroItems[player][index] = "None"
        case cardEffect.IronResolve:
            playerEffects[activePlayer].append("Iron Resolve")
        case cardEffect.MightyBlade:
            playerEffects[activePlayer].append("Mighty Blade")
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
            indeces = []
            if Cards[player][playerHand[-1]]["Card Type"] == cardType.Item:
                indeces.append(-1)
            if Cards[player][playerHand[-2]]["Card Type"] == cardType.Item:
                indeces.append(-2)
            finalIndex = int(input())
            playItem(finalIndex, playerHand[player][finalIndex],player)
            return
        case cardEffect.SeriousGrey:
            destroy(chooseHero(),choosePlayer())
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
            destroy(chooseHero(),chooseHero(),choosePlayer(),True,player)
        case cardEffect.SilentShadow:
            target = choosePlayer()
            for i in range(0,len(playerHand[target])):
                print(playerHand[target][i]) #Reveal
            index = int(input())
            playerHand[player].append(playerHand[target][index].pop())
        case cardEffect.SlipperyPaws:
            target = choosePlayer
            pullCard(target)
            pullCard(target)
            discardSpecific(target=player)
        case cardEffect.SmoothMimimeow:
            for i in range(0,playerCount):
                if i == player:
                    continue
                if len(playerHand[j]) > 0:
                    for j in range(0,len(playerHeroes[i])):
                        if Cards[playerHeroes[i][j]]["Class"] == heroType.Thief:
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
            if playerHand[activePlayer][-1] == cardType.Magic:
                if askPlayer():
                    playMagic(-1,player)
                    drawCard()
        case cardEffect.Spooky:
            for i in range(0,playerCount):
                if i == player:
                    continue
                if playerHeroes[i]:
                    sacrifice(i)             
        case cardEffect.Whiskers:
            stealHero(player,choosePlayer())
            destroy(chooseHero(),chooseHero(),choosePlayer())
        case cardEffect.Wiggles:
            stealHero(player,choosePlayer())
            activateHeroAbility(playerHeroes[player][-1],player=player)
        case cardEffect.BigBuckley:
            attack(True)
        case cardEffect.BuckOmens:
            target = int(input())
            for i in range(0,len(playerHand[target])):
                print(playerHand[target][i])
            index = int(input())
            playerHand[player].append(playerHand[target][index].pop())
            playHero(playerHand[player][-1],player,False)
        case cardEffect.DoeFallow:
            sacrifice(player)
            count = 7-len(playerHand[player])
            drawCard(count,player)
        case cardEffect.Maegisty:
            playerEffects[player].append("Maegisty")
        case cardEffect.MagusMoose:
            searchDiscard(cardType.Hero,player)
            if askPlayer():
                playHero(playerHand[player][-1],player,False)
        case cardEffect.Majestelk:
            sacrifice(player)
            playerEffects[player].append("Majestelk")
        case cardEffect.Stagguard:
            playerEffects[player].append("Stagguard")
        case cardEffect.BlindingBlade:
            target = int(input)
            for i in range(0,len(heroItems[target])):
                playerHand[target].append(heroItems[target][i].pop())
        case cardEffect.CriticalFang:
            playerEffects[player].append("Critical Fang")
        case cardEffect.HardenedHunter:
            count = 0
            for i in range(0,playerCount):
                if i == player:
                    continue
                count += len(playerMonsters[i])
            drawCard(count,player)
        case cardEffect.LootingLupo:
            drawCard(len(heroItems[player],player))
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
            for i in range(0,playerCount):
                if len(playerHeroes) > 2:
                    sacrifice(i)
        case cardEffect.GruesomeGladiator:
            for i in range(0,playerCount):
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
                destroy(chooseHero(),chooseHero(),choosePlayer(),activator=player)
        case cardEffect.RoaryalGuard:
            chosenClass = int(input())
            for i in range(0,playerCount):
                for j in range(0,len(playerHeroes[i])):
                    if playerHeroes[i][j]["Class"] == chosenClass:
                        playerHand[i].append(playerHeroes[i].pop(j))
                        discardPile.append(heroItems[i].pop(j))
        case cardEffect.ViciousWildcat:
            index = int(input())
            playerMonsters[player].append(monsterField.pop(index))
            AP = 0
        case cardEffect.UnbridledFury:
            heroDestroyed = destroy(chooseHero(),chooseHero(),choosePlayer(),activator = player)
            if Cards[heroDestroyed]["Class"] == heroType.Berserker:
                AP += 1
        case cardEffect.BarkHexer:
            allPlayersDiscard(True)
            allPlayersDiscard(False)
        case cardEffect.BeholdenRetriever:
            sacrifice(player)
            searchDiscard(cardType.Item,player,cardType.Hero)
        case cardEffect.BoneCollector:
            sacrificeItem(player)
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
            for i in range(0,playerCount):
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
            for i in range(0,playerCount):
                for j in range(0,len(playerHeroes[i])):
                    if Cards[playerHeroes[i][j]]["Class"] == heroType.Sorcerer:
                        playerHand[i].append(playerHeroes[i][j].pop())
                        discardPile.append(heroItems[i][j].pop())
        case cardEffect.Luut:
            target = choosePlayer()
            index = chooseHero(target)
            destination = chooseHero(player)
            heroItems[player][destination],heroItems[target][index] = heroItems[target][index],"None"
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
            target = choosePlayer
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
            for i in range(0,playerCount):
                for j in range(0,len(playerHeroes[i])):
                    if Cards[playerHeroes[i][j]] == "Hamlet" and i == player:
                        continue
                    if Cards[playerHeroes[i][j]]["Class"] == heroType.Bard:
                        playerHand[i].append(playerHeroes[i][j])
        case cardEffect.Hoodwink:
            target = choosePlayer()
            index = chooseHero()
            secondTarget = choosePlayer()
            secondIndex = chooseHero()
            heroItems[target][index],heroItems[secondTarget][secondIndex] = heroItems[secondTarget][secondIndex],heroItems[target][index]
        case cardEffect.PurringBandit:
            for i in range(0,playerCount):
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
        case cardEffect.FirepalceFugitive:
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
            playCards(activePlayer,2,type=Cards[hero]["Search Target"])
    return

def playCards(target = activePlayer,count: int = 1,type=cardType.Any) -> None: #When you are forced to (aka given the option)
    index = int(input)
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

def playMagic(index,target: int = activePlayer) -> None: #Play a magic card from your hand. Target is who it's used on
    global AP 
    discardPile.append(playerHand[target][index].pop())
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
            for i in range(0,playerCount):
                for i in range(0,len(heroItems[i])):
                    playerHand[i].append(heroItems[i].pop())
        case cardEffect.BeastCall:
            monsterDeck.insert(0,monsterField[1])
            monsterDeck.insert(0,monsterField[2])
            monsterDeck.insert(0,monsterField[3])
            monsterField[1] = monsterDeck.pop()
            monsterField[2] = monsterDeck.pop()
            monsterField[3] = monsterDeck.pop()
            AP += 1
        case cardEffect.RapidRefresh:
            discardHand()
            drawCard(4)
        case cardEffect.LightningLabrys:
            count = int(input())
            if count > len(playerHand[activePlayer]):
                count = len(playerHand())
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

def playItem(index, item, target:int = activePlayer) -> None:
    if heroItems[target][index]:
        if testingPhase:
            print("An Item is already equipped")
        return
    if not "Warworn Owlbear" in playerMonsters[target]:
        challenge()
    heroItems[target][index] = item
    if item == "Morph Mask":
        roll = rollDie()
        match(roll):
            case 1:
                morphMaskType[target][index] = heroType.Fighter
            case 2:
                morphMaskType[target][index] = heroType.Ranger
            case 3:
                morphMaskType[target][index] = heroType.Thief
            case 4:
                morphMaskType[target][index] = heroType.Guardian
            case 5:
                morphMaskType[target][index] = heroType.Ranger
            case 6:
                morphMaskType[target][index] = heroType.Wizard
    elif item == "Chaos Mask":
        roll = random.randint(1,6) + random.randint(1,6)
        match(roll):
            case 1 | 2 | 3:
                morphMaskType[target][index] = heroType.Warrior
            case 4 | 5 | 6:
                morphMaskType[target][index] = heroType.Druid
            case 7 | 8 | 9:
                morphMaskType[target][index] = heroType.Berserker
            case 10 | 11 | 12:
                morphMaskType[target][index] = heroType.Necromancer
    if "Wicked Sea Serpent" in playerMonsters[target]:
        drawCard(player=target)
    #Check if you won after equipping a class changing item
    if Cards[item]["Effect"] == cardEffect.Mask: getPartyCounts(target)
    return

def playHero(index,player=activePlayer,loseAP: bool = True) -> None:
    if loseAP:
        reduceAP()
    challenge()
    if gamemode == 1:
        playerHeroes[player].append(playerHand[index].pop())
    elif gamemode == 2 and len(playerHeroes[player]) == 5:
        tribute = int(input())
        playerHeroes[player][tribute] = playerHand[index]
        playerHand[index].pop()
    if len(heroItems[player]) < playerHeroes[player]: #Just some index stuff so playing an item works
        heroItems.append("None")
    activateHeroAbility(playerHand[index],index, summoned = True)
    return

def trade(index: int, target: int, selfTarget: int) -> None:
    #Swap the heroes
    playerHeroes[target][index],playerHeroes[activePlayer][selfTarget] = playerHeroes[activePlayer][selfTarget],playerHeroes[target][index]
    #Swap the items
    heroItems[target][index],heroItems[activePlayer][selfTarget] = heroItems[activePlayer][selfTarget],heroItems[target][index]
    return

def checkHeroSlot(slot,player,key) -> bool:
    return playerHeroes[player][slot] == key

def askPlayer(output: str = "") -> bool: #A yes or no prompt
    if bool(input(output)): return True
    return False

def choosePlayer(req: str = "") -> int:
    if playerCount == 2: 
        player = not(activePlayer - 1) + 1
        oneOpponent = True
    otherPlayer = player
    if testingPhase: return 2
    match(req):
        case "hasCard": #has card in hand
            try: player = int(input())
            except not playerHand[player] or (not playerHand[otherPlayer] and playerCount == 2):
                choosePlayer(req = "hasCard")   
        case "hasHero":
            try: player = int(input())
            except not playerHeroes[player] or (not playerHeroes[otherPlayer] and playerCount == 2):
                choosePlayer(req = "hasHero")
        case "": #Non-specific, no requirements
            if playerCount == 2: 
                return player
            else:
                player = int(input)
    return player
    
def chooseHero(player=activePlayer) -> int:
    index = int(input())
    return index

def challenge() -> bool:
    #TODO
    global panguardian
    if "Mighty Blade" in playerEffects[activePlayer]:
        return
    hasChallenge = []
    for i in range(0,playerCount):
        if i == activePlayer:
            continue
        if hasCardEffect(cardEffect.Challenge,i):
            hasChallenge.append(i)
    for i in range(0,len(hasChallenge)):
        if askPlayer():
            discardSpecific(cardType.Challenge,1,i,False)
            player = i
    mainRoll = rollDice()
    if playerLeaders[activePlayer] == "Fist of Reason":
        mainRoll += 2
    challengeRoll = rollDice()
    if playerLeaders[player] == "Fist of Reason":
        challengeRoll += 2
    if playerLeaders[player] == "Fierce Panguardian":
        panguardian = False
    if "Bloodwing" in playerMonsters[activePlayer]:
        discardSpecific(target=player)
    mainRoll += "Titan Wyvern" in playerMonsters[activePlayer]
    challengeRoll += "Titan Wyvern" in playerMonsters[player]

    if "Possessed Plush" in playerMonsters[player]:
        drawCard(player=player)
    if mainRoll < challengeRoll:
        return False
    #Fist of Reason gives +2
    return True

def hasModifier() -> list[int]:
    hasChallenge:int = []
    stagguardPlayer = -1
    for i in range(0,playerCount):
        if "Stagguard" in playerEffects[i]:
            stagguardPlayer: int = i
    for j in range(1,playerCount+1):
        if not(stagguardPlayer == -1 or i == stagguardPlayer):
            continue
        for i in range(0,len(playerHand[j])):
            if Cards[playerHand[j][i]]["Card Type"] == cardType.Modifier:
                hasChallenge.append(j)
    return hasChallenge

netModifier: int = 0
def modifier(player: int = activePlayer) -> int:
    count: int = 0
    global netModifier
    if not askAllToModifyOrChallenge:
        listPlayers: list[int] = hasModifier()
        for i in range(0,len(listPlayers)):
            if askPlayer(useModifier):
                netModifier += playModifier(listPlayers[i])
                count += 1
                if i != activePlayer and "Abyss Queen" in playerMonsters[activePlayer]:
                    netModifier += 1
    else:
        for i in range(1,playerCount+2):
            if askPlayer(output=useModifier):
                netModifier += playModifier(i)
                count += 1
                if i != activePlayer and "Abyss Queen" in playerMonsters[activePlayer]:
                    netModifier += 1
    if netModifier != 0:
        for i in range(0,playerCount):
            if "Crowned Serpent" in playerMonsters[i]:
                drawCard(player = i)
    for i in range(0,playerCount):
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
    for i in range(0,len(playerHand[player])):
        if Cards[playerHand[player][i]]["Card Type"] == cardType.Modifier:
            hasModifier == True
    if not hasModifier:
        if testingPhase: print("You don't have a modifier")
        return 0
    index = int(input("Which Card: "))
    boostSign = int(input("+ or - (1 or 0): "))
    boost: int = 0
    if boostSign == 1:
        boost = Cards[playerHand[player][index]]["Positive Effect"]
    else:
        boost -= Cards[playerHand[player][index]]["Negative Effect"]
    discardPile.append(playerHand[player].pop(index))
    if playerLeaders[player] == "Protecting Horn":
        bonus = input()
        match(bonus):
            case 0:
                boost += 1
            case 1:
                boost -= 1
            case _:
                return boost
    return boost

def hasCardEffect(effect,player=activePlayer) -> bool:
    for i in range(0,len(playerHand[player])):
        if Cards[playerHand[player][i]]["Effect"] == effect:
            return True
    return False

def pullCard(target: int = activePlayer,reqType: int = cardType.Any, revealHand: bool = False) -> bool:
    #target is who is stolen from, req is true/false for if there is a requirement, reqType is what card type you need to pull or else you dont pull
    index = -1
    if revealHand:
        for i in range(0,len(playerHand[target])):
            print(playerHand[target][i])
        index = int(input())
    else:
        random.shuffle(playerHand[target])
    pulledCard: str = playerHand[target].pop(index)
    if testingPhase:
        print(f"Pulled Card: {pulledCard}")
    playerHand[activePlayer].append(pulledCard)
    return (Cards[pulledCard]["Class"] == reqType)#return if it matched the type you were looking for

def searchDiscard(cardType = cardType.Any, player: int = activePlayer, alternateCardType = cardType.Any) -> None:
    return

def revealCard(index: int, player: int = activePlayer) -> None:
    print(playerHand[player][index])
    return

def whichCard(matchType,typeToMatch) -> int:
    return

def checkHand(cardType, player=activePlayer) -> None:
    for card in playerHand[player]:
        if Cards[(playerHand[player][card])]["Card Type"] == cardType:
            return True
    return False

def checkField() -> bool:
    return

def handSize(player=activePlayer) -> int:
    return len(playerHand[player])

def viewHand(player) -> None:
    return

def mill(numMilled, target=activePlayer) -> None:
    #mainDeck
    return

def destroy(index,target,player: int = activePlayer, shurikitty: bool = False,activator: int = activePlayer) -> int: #target should be the index of the card
    #Always pops item, but only pops item if it has Decoy Doll
    heroDestroyed = 0
    if "Terratuga" in playerMonsters[target]: return heroDestroyed
    if not "Corrupted Sabretooth" in playerMonsters[player]: #TODO
        discardPile.append(heroItems[target][index].pop())
        if heroItems[target][index] != "Decoy Doll": #Protects the hero
            if "Maegisty" in playerEffects[player]:
                playerHand[player].append(playerHeroes[target][index].pop())
            else:
                heroDestroyed = playerHeroes[target][index]
                discardPile.append(playerHeroes[target][index].pop())
        #TODO effects that happen after destroyed 
        if playerLeaders[target] == "Brutal Bow":
            drawCard(1)
        for i in range(0,len(playerHeroes[target])):
            if heroItems[target][i] == "Soul Tether":
                if "Maegisty" in playerEffects[player]:
                    playerHand.append(playerHeroes[target][i].pop())
                else:
                    discardPile.append(playerHeroes[target][i].pop())
                if not shurikitty:
                    discardPile.append(heroItems[target][i].pop())
                else:
                    playerHand[activator].append(heroItems[target][i].pop())
        if "Dracos" in playerMonsters[target]:
            drawCard(player = target)
        if "Wandering Behemoth" in playerMonsters[target]:
            drawCard(player = target)
    #else:
    return heroDestroyed

def sacrificeItem(target: int = activePlayer, count: int = 1) -> None:
    index = int(input())
    discardPile.append(heroItems[index].pop())
    return

def sacrificeSpecific(target: int = activePlayer,index: int = -1) -> None:
    hasHero = False #in hand
    if "Dragon Wasp" in playerMonsters[target]:
        if askPlayer():
            discardSpecific(count=2,target=target,canCancel=False)
            return
    if "Maegisty" in playerEffects[target]:
        playerHand.append(playerHeroes[target][index].pop())
        discardPile.append(heroItems[target][index].pop())
    else:
        discardPile.append(playerHeroes[target][index].pop())
        discardPile.append(heroItems[target][index].pop())
    for i in range(0,len(playerHeroes[target])):
        if heroItems[target][i] == "Soul Tether":
            if "Maegisty" in playerEffects[target]:
                playerHand.append(playerHeroes[target][index].pop())
            else:
                discardPile.append(playerHeroes[target][index].pop())
            discardPile.append(heroItems[target][i].pop())
            discardPile.append(heroItems[target][index].pop())
    if WarriorsAndDruids:
        for i in range(0,playerCount):
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

def sacrifice(target: int = activePlayer,heroType=heroType.Any, count: int = 1, forcedIndex: int = 0) -> None:
    hasHero = False #in hand
    if "Dragon Wasp" in playerMonsters[target]:
        if askPlayer():
            discardSpecific(count=2,target=target,canCancel=False)
            return
    for i in range(0,count):
        index = chooseHero(target, heroType)
        if "Maegisty" in playerEffects[target]:
            playerHand.append(playerHeroes[target][index].pop())
            discardPile.append(heroItems[target][index].pop())
        else:
            discardPile.append(playerHeroes[target][index].pop())
            discardPile.append(heroItems[target][index].pop())
    for i in range(0,len(playerHeroes[target])):
        if heroItems[target][i] == "Soul Tether":
            if "Maegisty" in playerEffects[target]:
                playerHand.append(playerHeroes[target][index].pop())
            else:
                discardPile.append(playerHeroes[target][index].pop())
            discardPile.append(heroItems[target][i].pop())
            discardPile.append(heroItems[target][index].pop())
    if WarriorsAndDruids:
        for i in range(0,playerCount):
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

def stealHero(playerDestination: int = activePlayer, playerTarget: int = activePlayer) -> None:
    if playerCount == 2 and "Calming Voice" in playerEffects[not(activePlayer-1)+1]:
        print("Cannot steal a hero from this player by Calming Voice's effect")
        return
    if playerTarget == activePlayer:
        try:
            playerTarget = choosePlayer()
        except "Calming Voice" in playerEffects[playerTarget]:
            stealHero(playerDestination)
    index = int(input())
    playerHeroes[playerDestination].append(playerHeroes[playerTarget][index].pop())
    heroItems[playerDestination].append(heroItems[playerTarget][index].pop())
    if WarriorsAndDruids:
        for i in range(0,len(playerHeroes[playerTarget])):
            if heroItems[playerTarget][i] == "Cursed Glove":
                playerHeroes[playerDestination].append(playerHeroes[playerTarget][i].pop())
                heroItems[playerDestination].append(heroItems[playerTarget][i].pop())
    return

def checkHeroItem() -> int:
    return

def giveCard() -> None:
    return

def tradeHands(targetOne: int = activePlayer, targetTwo: int = not(activePlayer-1)+1) -> None:
    playerHand[targetOne], playerHand[targetTwo] = playerHand[targetTwo], playerHand[targetOne]
    return

def checkDrawn():
    return

def returnCardToHand(cardType,target=activePlayer):
    return

def equipItem() -> None:
    return

def allPlayersDiscard(hitSelf: bool = True, type=cardType.Any) -> None:
    for i in range(1,playerCount+1):
        if hitSelf or i != activePlayer:
            discardSpecific(type,1,1)
    return

def addFromDiscard(count: int = playerCount-1, player: int = activePlayer) -> None:
    for i in range(count-1,-1,-1):
        print(discardPile[i])
    index = int(input())
    playerHand[player].append(discardPile.pop(-index))
    return

def protectionStatus(player=activePlayer) -> bool: #Will probably remove
    return

def draw() -> None: #Spend AP and draw a card as an action
    if not ("Muscipula Rex" in playerMonsters[activePlayer] and not muscipulaRex):
        reduceAP()
    if not "Lumbering Demon" in playerMonsters[activePlayer]:
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
    random.shuffle(mainDeck)
    return

def drawCard(count: int = 1, player: int = activePlayer) -> None:
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
            discardPile.append(playerHand[player][discardIndex].pop())
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
    if not checkAtkRequirements(monsterField[monster]) and not "Nimble Gray" in playerEffects[activePlayer]:
        print("Doesn't meet Party Requirements")
        return
    if not dontLoseAP:
        reduceAP(2)
    diceRoll = rollDice()
    diceRoll += (playerLeaders[activePlayer] == "Divine Arrow" or (playerLeaders[activePlayer] == "Unstable Unicorn" and playerLeaders[unstableUnicornTarget[activePlayer]] == "Divine Arrow"))
    if "Reptilian Ripper" in playerMonsters[activePlayer]:
        diceRoll += 2
    if "Ancient Megashark" in playerMonsters[activePlayer]:
        diceRoll += 1
    if "Critical Fang" in playerEffects[activePlayer]:
        diceRoll += 4
    for player in range(0,playerCount): #Checks all player parties
        if player == activePlayer: #Don't apply the negative to yourself
            continue
        if "Chitin Scourge" in playerMonsters[player]:
            diceRoll -= 1
    if testingPhase:
        diceRoll = 12
    print(f"Rolled a: {diceRoll}")
    if diceRoll >= Monsters[monsterField[monster]]["Win Roll"]:
        effect = Monsters[monsterField[monster]]["Win Effect"]
    elif diceRoll <= Monsters[monsterField[monster]]["Lose Roll"]:
        effect = Monsters[monsterField[monster]]["Lose Effect"]
    else:
        effect = monsterRollEffect.noEffect
    if testingPhase:
        print(f"Effect: {effect}")
    if playerLeaders[activePlayer] == "Rhythmic Archer" or (playerLeaders[activePlayer] == "Unstable Unicorn" and playerLeaders[unstableUnicornTarget[activePlayer]] == "Rhythmic Archer"):
        if effect != monsterEffect.slay:
            drawCard()
    
    match(effect):
        case monsterRollEffect.slay:
                if len(playerMonsters[activePlayer-1]) < 2:
                    if playerLeaders[activePlayer] == "Raging Manticore" or (playerLeaders[activePlayer] == "Unstable Unicorn" and playerLeaders[unstableUnicornTarget[activePlayer]] == "Raging Manticore"):
                        drawCard()
                    #Copy the card to the player's field and then replace it with one from the Deck
                    print(f"Monster attacked: {monsterField[monster]}")
                    playerMonsters[activePlayer-1].append(monsterField[monster])
                    print(f"Player {activePlayer}'s Monsters: {playerMonsters[activePlayer-1]}")
                    if testingPhase:
                        print(f"{monsterField[monster]} was slain by Player {activePlayer}")
                    monsterField[monster] = monsterDeck.pop()
                    if testingPhase:
                        print(f"Monsters: {monsterField}")
                    monsterField[monster] = monsterDeck.pop()
                    if playerLeaders[activePlayer] == "Raging Manticore":
                        drawCard(2)
                    if testingPhase:
                        print(f"Monsters: {monsterField}")
                else:
                    endGame("Monsters")
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

def endGame(typeOfWin: str, winningPlayer: int = activePlayer) -> None:
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

def selectMonster() -> int: #TODO
    try:
        index = int(input("Which Monster: ")) - 1
    except index < 0 or index > 2:
        selectMonster()
    return index

def checkAtkRequirements(monster) -> bool:
    heroCount, classSet = getPartyCounts()
    if heroCount < Monsters[monster]["Hero Req"]:
        if testingPhase:
            heroReq = Monsters[monster]["Hero Req"]
            print(f"Not enough Heroes: {heroCount} out of {heroReq}")
        return False
    if (Monsters[monster]["Class Req"] != heroType.NoClass) and not (Monsters[monster]["Class Req"] in classSet):
        if testingPhase:
            classReq = Monsters[monster]["Class Req"]
            print(f"No Hero of class {classReq}")
        return False
    return True

def getPartyCounts(target: int = activePlayer) -> tuple[int,list]: #Returns an int value and a list of enum'd ints
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

def discardHand(player=activePlayer) -> None:
    if not playerHand[activePlayer]: return #Return if empty
    handSize = len(playerHand[player])
    for card in range(0,handSize):
        discardPile.append(playerHand[player].pop())
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

def discardSpecific(type=cardType.Any,count=1,target=activePlayer, canCancel: bool = False) -> int:
    if not playerHand[target]: return
    if len(playerHand[target]) < count: count = len(playerHand[target])
    for i in range(0,count):
        cardIndex = selectFromHand(type,target, canCancel)
        if cardIndex == -1:
            count = i
            continue
        discardSelected(cardIndex,target)
    return count

def selectFromHand(type=cardType.Any,target=activePlayer, canCancel: bool = False) -> int:
    cancelled = False #If the player wants to cancel
    try:
        index = int(input()) #TODO
    except type != playerHand[target][index]:
        selectFromHand(type,target)
    except cancelled and canCancel:
        return -1
    return index

def discardSelected(cardIndex,target=activePlayer) -> None:
    discardPile.append(playerHand[target][cardIndex].pop())
    for i in range(0,playerCount):
        if "Razor Tongue" in playerMonsters[i] and i != target:
            drawCard(player=i) #TODO This will have issues
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
