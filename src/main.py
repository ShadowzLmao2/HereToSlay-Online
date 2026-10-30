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
gameEnded = False
silverLining = False

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
def main(test: str = "None") -> None:
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
        global silverLining
        silverLining = False
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

def rollDice() -> int:
    return random.randint(1,6) + random.randint(1,6)

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
    global AP, silverLining
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
    diceRoll = rollDice()
    if heroItems[player][index] != "None":
        diceRoll += playerLeaders[player] == "Charismatic Song" or playerLeaders[unstableUnicornTarget[player]] == "Charismatic Song"
        diceRoll += 2*(heroItems[player][index] == "Really Big Ring")
        diceRoll += 4*(heroItems[player][index] == "Even Bigger Ring")
        diceRoll += 2*silverLining
        diceRoll -= 2*(heroItems[player][index] == "Cursed of the Snake's Eyes")
        if heroItems[player][index] == "Biggest Ring Ever":
            for i in range(0,3):
                index = selectFromHand(cardType.Any,player,canCancel=True)
                if index == -1:
                    continue
                else:
                    discardSelected(index,player)
                    diceRoll += 2
        elif heroItems[player][index] == "Mysterious Feather":
            index = selectFromHand(cardType.Any,player,canCancel=True)
            if index != -1:
                discardSelected(index,player)
                diceRoll += 3

    #apply modifiers here
    if  diceRoll >= Cards[playerHeroes[player][index]]["Effect Roll"]:
        activatedHeroAbility[index] = True
        if heroItems[player][index] == "Suspiciously Shiny Coin":
            discardSpecific()
        useHeroAbility(playerHeroes[player][index])
    elif heroItems[player][index] != "None":
        if heroItems[player][index] == "Particularly Rusty Coin":
            drawCard(1)
        elif heroItems[player][index] == "Temporal Hourglass":
            AP += 1
        elif heroItems[player][index] == "Goblet of Caffeination":
            if askPlayer():
                discardPile.append(heroItems[player][index])
                heroItems[player][index] = "None"
        elif heroItems[player][index] == "Silver Lining":
            silverLining = True
        elif heroItems[player][index] == "Dragon's Bile":
            sacrifice(target=player)
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
        match Leaders[leader]["Effect"]:
            case leaderEffect.ShadowClaw:
                target = choosePlayer(1)
                #Need to get a target in the hand. will do rand for now
                pullCard(target, False, 0)
                reduceAP()
                leaderAbilityUsed = True
                return
            case leaderEffect.GnawingDread:
                index = searchDiscard(cardType.Any)
                reduceAP(2)
                playerHand[activePlayer].append(discardPile[index].pop())
                leaderAbilityUsed = True
                return
            case leaderEffect.IllusiveTrickster:
                if checkHand(cardType.Magic, activePlayer):
                    discardSpecific(cardType.Magic,1)
                    drawCard(3)
                    leaderAbilityUsed = True
                return
    return

def useHeroAbility(hero) -> None:
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
            playCard(cardType.Hero,False)
        case cardEffect.GreedyCheeks:
            return
        case cardEffect.LuckyBucky:
            
            return
        case cardEffect.MellowDee:
            return
        case cardEffect.TipsyTootie:
            index = int(input())
            selfIndex = int(input())
            trade(index, choosePlayer(), selfIndex)
        case cardEffect.CalmingVoice:
            return
        case cardEffect.HolyCurselifter:
            return
        case cardEffect.IronResolve:
            return
        case cardEffect.MightyBlade:
            return
        case cardEffect.VibrantGlow:
            return
        case cardEffect.WiseShield:
            return
        case cardEffect.Bullseye:
            return
        case cardEffect.Hook:
            return
        case cardEffect.QuickDraw:
            return
        case cardEffect.SeriousGrey:
            return
        case cardEffect.SharpFox:
            return
        case cardEffect.Wildshot:
            return
        case cardEffect.WilyRed:
            return
        case cardEffect.Meowzio:
            return
        case cardEffect.PlunderingPuma:
            return
        case cardEffect.Shurikitty:
            return
        case cardEffect.SilentShadow:
            return
        case cardEffect.SlipperyPaws:
            return
        case cardEffect.SmoothMimimeow:
            return
        case cardEffect.BunBun:
            return
        case cardEffect.Fluffy:
            return
        case cardEffect.Hopper:
            return
        case cardEffect.Snowball:
            return
        case cardEffect.Spooky:
            return
        case cardEffect.Whiskers:
            return
        case cardEffect.Wiggles:
            return
        case cardEffect.BigBuckley:
            return
        case cardEffect.BuckOmens:
            return
        case cardEffect.DoeFallow:
            return
        case cardEffect.Majestelk:
            return
        case cardEffect.MagusMoose:
            return
        case cardEffect.Maegisty:
            return
        case cardEffect.Stagguard:
            return
        case cardEffect.BlindingBlade:
            return
        case cardEffect.CriticalFang:
            return
        case cardEffect.HardenedHunter:
            return
        case cardEffect.LootingLupo:
            return
        case cardEffect.SilentShield:
            return
        case cardEffect.TenaciousTimber:
            return
        case cardEffect.WolfgangPack:
            return
        case cardEffect.Annihilator:
            return
        case cardEffect.BrawlingSpirit:
            return
        case cardEffect.GruesomeGladiator:
            return
        case cardEffect.Meowntain:
            return
        case cardEffect.RabidBeast:
            return
        case cardEffect.RoaryalGuard:
            return
        case cardEffect.ViciousWildcat:
            return
        case cardEffect.UnbridledFury:
            return
        case cardEffect.BarkHexer:
            return
        case cardEffect.BeholdenRetriever:
            return
        case cardEffect.BoneCollector:
            return
        case cardEffect.BostonTerror:
            return
        case cardEffect.GrimPupper:
            return
        case cardEffect.HollowHusk:
            return
        case cardEffect.PerfectVessel:
            return
        case cardEffect.ShadowSaint:
            return
        case cardEffect.Dystortivern:
            return
        case cardEffect.Extraga:
            return
        case cardEffect.Dragalter:
            return
        case cardEffect.Luut:
            return
        case cardEffect.Renovern:
            return
        case cardEffect.Mirroryu:
            return
        case cardEffect.Smok:
            return
        case cardEffect.Oracon:
            return
        case cardEffect.Shamanaga:
            return
        case cardEffect.Bearserker:
            return
        case cardEffect.Hamlet:
            return
        case cardEffect.ComplexIllusion:
            return
        case cardEffect.Enchantler:
            return
        case cardEffect.Hoodwink:
            return
        case cardEffect.PurringBandit:
            return
        case cardEffect.NimbleGray:
            return
        case cardEffect.Mimi:
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

def playCards(target = activePlayer,count: int = 1,pickAll: bool = False,type=cardType.Any) -> None: #When you are forced to (aka given the option)
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
    discardPile.append(playerHand[target][index].pop())
    match(Cards[playerHand[target][index]]["Effect"]):
        case cardEffect.CallToTheFallen:
            return
        case cardEffect.CriticalBoost:
            return
        case cardEffect.DestructiveSpell:
            return
        case cardEffect.EnchantedSpell:
            return
        case cardEffect.EntanglingTrap:
            return
        case cardEffect.ForcedExchange:
            selfIndex = int(input())
            target = int(input(targetStr))
            trade(index,choosePlayer(),selfIndex)
            return
        case cardEffect.WindsOfChange:
            return
        case cardEffect.BeastCall:
            return
        case cardEffect.RapidRefresh:
            return
        case cardEffect.LightningLabrys:
            return
        case cardEffect.MassSacrifice:
            return
        case cardEffect.EggOfFortune:
            return
        case cardEffect.CaptivatingSpell:
            return
    return

def playItem(index, item, target:int = activePlayer) -> None:
    if heroItems[target][index]:
        if testingPhase:
            print("An Item is already equipped")
        return
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
        roll = rollDice()
        match(roll):
            case 1 | 2 | 3:
                morphMaskType[target][index] = heroType.Warrior
            case 4 | 5 | 6:
                morphMaskType[target][index] = heroType.Druid
            case 7 | 8 | 9:
                morphMaskType[target][index] = heroType.Berserker
            case 10 | 11 | 12:
                morphMaskType[target][index] = heroType.Necromancer
    #Check if you won after equipping a class changing item
    if Cards[item]["Effect"] == cardEffect.Mask: getPartyCounts(target)
    return

def playHero(index,player=activePlayer) -> None:
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
        canModify = False
    if "Bloodwing" in playerMonsters[activePlayer]:
        discardSpecific(cardType.Any,1,player)
    mainRoll += "Titan Wyvern" in playerMonsters[activePlayer]
    challengeRoll += "Titan Wyvern" in playerMonsters[player]
    if mainRoll < challengeRoll:
        return False
    #Fist of Reason gives +2
    return True

def hasModifier() -> list[int]:
    hasChallenge:int = []
    for j in range(1,playerCount+1):
        for i in range(0,len(playerHand[j])):
            if Cards[playerHand[j][i]]["Card Type"] == cardType.Modifier:
                hasChallenge.append(j)
    return hasChallenge

netModifier: int = 0
def modifier() -> int:
    global netModifier
    if not askAllToModifyOrChallenge:
        listPlayers: list[int] = hasModifier()
        for i in range(0,len(listPlayers)):
            if askPlayer(useModifier):
                netModifier += playModifier(listPlayers[i])
    else:
        for i in range(1,playerCount+2):
            if askPlayer(output=useModifier):
                netModifier += playModifier(i)
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
    return boost

def hasCardEffect(effect,player=activePlayer) -> bool:
    for i in range(0,len(playerHand[player])):
        if Cards[playerHand[player][i]]["Effect"] == effect:
            return True
    return False

def pullCard(target,reqType=0) -> bool:
    #target is who is stolen from, req is true/false for if there is a requirement, reqType is what card type you need to pull or else you dont pull
    pulledCard: str = playerHand[target].pop()
    if testingPhase:
        print(f"Pulled Card: {pulledCard}")
    playerHand[activePlayer].append(pulledCard)
    return (Cards[pulledCard]["Class"] == reqType)#return if it matched the type you were looking for

def searchDiscard(cardType):
    return

def playCard(type,optional=True) -> None:
    if checkHand(type,activePlayer):
        if optional:
            if askPlayer() == False:
                placeCard()
                removeFromHand()
                return
    else:
        whichCard(True,type)
        placeCard()
        removeFromHand()
    if type == cardType.Magic and playerLeaders[activePlayer] == "Cloaked Sage":
        drawCard(1)
    return

def revealCard(index: int, player: int = activePlayer) -> None:
    print(playerHand[player][index])
    return

def whichCard(matchType,typeToMatch) -> int:
    return

def removeFromHand() -> None:
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

def destroy(index,player) -> None: #target should be the index of the card
    #Always pops item, but only pops item if it has Decoy Doll
    discardPile.append(heroItems[player][index].pop())
    if heroItems[player][index] != "Decoy Doll":
        discardPile.append(playerHeroes[player][index].pop())
    #TODO effects that happen after destroyed 
    if playerLeaders[activePlayer] == "Brutal Bow":
        drawCard(1)
    for i in range(0,len(playerHeroes[player])):
        if heroItems[player][i] == "Soul Tether":
            discardPile.append(playerHeroes[player][i].pop())
            discardPile.append(heroItems[player][i].pop())
    return

def sacrifice(target: int = activePlayer,heroType=heroType.NoClass, count: int = 1) -> None:
    for i in range(0,count):
        index = chooseHero(target, heroType)
        discardPile.append(playerHeroes[target][index].pop())
    for i in range(0,len(playerHeroes[target])):
        if heroItems[target][i] == "Soul Tether":
            discardPile.append(playerHeroes[target][i].pop())
            discardPile.append(heroItems[target][i].pop())
    return

def stealHero(playerTarget, playerDestination, index) -> None:
    playerHeroes[playerDestination].append(playerHeroes[playerTarget][index].pop())
    if WarriorsAndDruids:
        for i in range(0,len(playerHeroes[playerTarget])):
            if heroItems[playerTarget][i] == "Cursed Glove":
                playerHeroes[playerDestination].append(playerHeroes[playerTarget][i].pop())
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
    reduceAP()
    drawCard(1)
    return

def drawCard(count, player=activePlayer) -> None: #Used in other functions
    for i in range(0,count,1):
        playerHand[player].append(mainDeck.pop())
    if testingPhase:
        print(f"Player {player} drew {count} card(s)")
        print(playerHand[player])
    return

def drawMonsterCard(count=1) -> None:
    for i in range(2,2-count,-1):
        monsterField[i] = monsterDeck[-1]
        monsterDeck.pop()
    if testingPhase:
        print(f"{count} Monster Card(s) were/was drawn")
        print(monsterField)
    return

def attack() -> None:
    if AP < 2:
        print("Not enough AP")
        return
    monster = selectMonster()
    if not checkAtkRequirements(monsterField[monster]):
        print("Doesn't meet Party Requirements")
        return
    reduceAP(2)
    diceRoll = rollDice()
    diceRoll += (playerLeaders[activePlayer] == "Divine Arrow" or (playerLeaders[activePlayer] == "Unstable Unicorn" and playerLeaders[unstableUnicornTarget[activePlayer]] == "Divine Arrow"))
    if "Reptilian Ripper" in playerMonsters[activePlayer]:
        diceRoll +=2
    if "Ancient Megashark" in playerMonsters[activePlayer]:
        diceRoll +=2
    for player in range(0,playerCount): #Checks all player parties
        if player == activePlayer: #Don't apply the negative to yourself
            continue
        if "Chitin Scourge" in playerMonsters[player]:
            diceRoll -=1
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
            drawCard(1)
    match(effect): #Note: No fallthrough
        case monsterRollEffect.slay:
                if len(playerMonsters[activePlayer-1]) < 2:
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
