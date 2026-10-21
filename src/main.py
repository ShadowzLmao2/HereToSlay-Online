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
playerCount = 4
gameEnded = False

#Separate from the GUI, handles the main game once you enter a game with another player
def startGame(test="None") -> None:
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
        global playerCount, activePlayer
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
    for hero in playerHeroes[activePlayer]: #setup stuff, to make it easier
        activatedHeroAbility[hero] = False
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
                if ranked:
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
    return random.int(1,6) + random.int(1,6)

def chooseAction() -> None:
    #Working: endTurn() draw() discardDraw() attack() 
    #WIP: activateHeroAbility(hero) activateLeaderAbility(leader)
    #TBC: playHero() 
    return

def activateHeroAbility(hero, index: int) -> None: 
    #hero is the card's enum. index is its spot on the field
    #will probably remove the hero input and replace with index
    if activatedHeroAbility[index]:
        if testingPhase:
            print("Ability already activated this turn")
        return
    if AP > 0:
        reduceAP()
        diceRoll = rollDice()
        #TODO Unstable Unicorn Stuff
        if playerLeaders[activePlayer] == "Charismatic Song":
            diceRoll +=1
        if  diceRoll >= Cards[hero]["Effect Roll"]:
            activatedHeroAbility[index] = True
            useHeroAbility(hero)
        else:
            if testingPhase:
                print("Failed the roll")
    else:
        print("No AP")
    return

#Used for useLeaderAbility
leaderAbilityUsed= False

def activateLeaderAbility(leader=playerLeaders[activePlayer]) -> None:
    #global leaderAbilityUsed
    #Sets the Unicorn's ability to whatever it copied at the start of the turn
    if leader == "Unstable Unicorn":
        leader = playerLeaders[(unstableUnicornTarget[activePlayer])]

    #Checks if it can be activated, pulls index of target leader so UU works
    if AP < Leaders[leader]["AP Cost"] or not Leaders[leader]["Activatable"] or leaderAbilityUsed:
        print("No AP or unable to use ability")
        return
    else:
        match Leaders[leader]["Effect"]:
            case leaderEffect.ShadowClaw:
                if ranked:
                    if (activePlayer == 1 and not playerHand[2]) or (activePlayer == 2 and not playerHand[1]):
                        return #No target
                    else: target = (not(activePlayer-1))+1
                else:
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
            return
        case cardEffect.PullCard:
            target = choosePlayer()
            pulledCard = pullCard(target,False,0)
            if Cards[pulledCard]["Class"] == Cards[hero]["Pull Type"]:
                pullCard(target,False,0)
            return
        case cardEffect.BearyWise:
            allPlayersDiscard(False, cardType.Any)
            #TODO player picks a card from the discarded
            return
        case cardEffect.ForceDiscard:
            discardSpecific(choosePlayer(),2,1)
            return
        case cardEffect.PanChucks:
            drawCard(2)
            firstDraw = playerHand[activePlayer][-2]
            secondDraw = playerHand[activePlayer][-1]
            if testingPhase:
                print("Drew", firstDraw, "and", secondDraw)
                if Cards[activePlayer][firstDraw]["Effect"] == cardEffect.Challenge:
                    revealCard(-2)
                    player = choosePlayer()
                    target = chooseHero()
                    destroy(target, player)
                if Cards[activePlayer][secondDraw]["Effect"] == cardEffect.Challenge:
                    revealCard(-1)
                    player = choosePlayer()
                    target = chooseHero()
                    destroy(target, player)
            return
        case cardEffect.QiBear:
            #discard up to 3, pop hero for each
            return
        case cardEffect.ToughTeddy:
            #Every player owning a fighter discards
            for i in range(1,playerCount,1):
                if i != activePlayer: #TODO check for a fighter
                    discardSpecific(cardType.Any,1,i)
            return
        case cardEffect.DodgyDealer:
            return
        case cardEffect.FuzzyCheeks:
            drawCard(1)
            playCard(cardType.Hero,False)
            return
        case cardEffect.GreedyCheeks:
            return
        case cardEffect.LuckyBucky:
            
            return
        case cardEffect.MellowDee:
            return
        case cardEffect.TipsyTootie:
            return
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
            return
        case cardEffect.SearchDiscard:
            searchDiscard(Cards[hero]["Search Target"])
            return
        case cardEffect.StealHero:
            stealHero()
            return
        case cardEffect.PullAndPlay:
            pullCard(choosePlayer(),True,Cards[hero]["Search Target"])
            return
        case cardEffect.Play2:
            playCards(activePlayer,2,False,Cards[hero]["Search Target"])
            return
    return

def playCards(target,count,pickAll,type) -> None:
    for i in range(0,count,1):
        match(type):
            case cardType.Hero:
                return
            case cardType.Magic:
                return
            case cardType.Item:
                return
    return

def summonHero(slot,hero,player=activePlayer) -> None:
    if AP > 0 and checkHeroSlot(slot,player,"None"):
        reduceAP()
        challenge()
        summon(slot,hero,player)
    return

def summon(slot,hero,player=activePlayer) -> None:
    playerHeroes[player][slot] = hero
    return

def checkHeroSlot(slot,player,key) -> bool:
    return playerHeroes[player][slot] == key

def askPlayer() -> bool:
    return

def choosePlayer(req=0) -> int:
    if ranked:
        if activePlayer == 1:
            return 0
        else:
            return 1
    else:
        if testingPhase: return 2
        #TODO
        #Req = 1, has card in hand
        return input()
    
def chooseHero(player=activePlayer) -> int:
    index = int(input())
    return index

def challenge() -> None:
    #Fist of Reason gives +2
    return hasCardEffect(cardEffect.Challenge)

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

def revealCard(index) -> None:
    return

def whichCard(matchType,typeToMatch) -> int:
    return

def removeFromHand() -> None:
    return

def placeCard() -> None:
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

def destroy(target,player) -> None: #target should be the index of the card
    discardPile.append(target)
    playerHeroes[player][target] = "None"
    #TODO effects that happen after destroyed 
    if playerLeaders[activePlayer] == "Brutal Bow":
        drawCard(1)
    return

def sacrifice(target=activePlayer,heroType=heroType.NoClass, count=1) -> None:
    for i in range(0,count):
        index = chooseHero(target, heroType)
        discardPile.append(playerHeroes[target][index].pop())
    return

def stealHero() -> None:
    return

def checkHeroItem() -> int:
    return

def giveCard() -> None:
    return

def tradeHands() -> None:
    return

def checkDrawn():
    return

def returnCardToHand(cardType,target=activePlayer):
    return

def equipItem() -> None:
    return

def allPlayersDiscard(hitSelf: bool, type=cardType.Any) -> None:
    for i in range(1,playerCount+1):
        if hitSelf or i != activePlayer:
            discardSpecific(type,1,1)
    return

def protectionStatus(player=activePlayer) -> bool: #Will probably remove
    return

def draw() -> None: #Spend AP and draw a card as an action
    if AP > 0:
        reduceAP()
        drawCard(1)
    else:
        print("No AP")
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
    if AP < 1:
        print("Not enough AP")
        return
    monster = selectMonster()
    if not checkAtkRequirements(monster):
        print("Doesn't meet Party Requirements")
        return
    reduceAP(2)
    diceRoll = rollDice()
    diceRoll += (playerLeaders[activePlayer] == "Divine Arrow" or (playerLeaders[activePlayer] == "Unstable Unicorn" and playerLeaders[unstableUnicornTarget[activePlayer]] == "Divine Arrow"))
    if "Reptilian Ripper" in playerMonsters[activePlayer]:
        diceRoll +=2
    if "Ancient Megashark" in playerMonsters[activePlayer]:
        diceRoll +=2
    for player in playerCount: #Checks all player parties
        if player == activePlayer: #Don't apply the negative to yourself
            continue
        if "Chitin Scourge" in playerMonsters[player]:
            diceRoll -=1
    if diceRoll >= Monsters[monster]["Win Roll"]:
        effect = Monsters[monster]["Win Effect"]
    elif diceRoll <= Monsters[monster]["Lose Roll"]:
        effect = Monsters[monster]["Lose Effect"]
    else:
        effect = monsterRollEffect.noEffect
    if playerLeaders[activePlayer] == "Rhythmic Archer" or (playerLeaders[activePlayer] == "Unstable Unicorn" and playerLeaders[unstableUnicornTarget[activePlayer]] == "Rhythmic Archer"):
        if effect != monsterEffect.slay:
            drawCard(1)
    match(effect): #Note: No fallthrough
        case monsterRollEffect.slay:
                if monstersSlain[activePlayer] < 3:
                    playerMonsters[activePlayer].append(Monsters[monster])
                    monstersSlain[activePlayer]  += 1
                    activeMonster[monster] = monsterDeck.pop()
                    if playerLeaders[activePlayer] == "Raging Manticore":
                        drawCard(2)
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
    index = int(input())
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
    heroCount = len(playerHeroes[target])
    classSet = set() #It's actually a set, no duplicates that way
    for card in range(0, heroCount):
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

def discardSpecific(type=cardType.Any,count=1,target=activePlayer) -> None:
    if not playerHand[target]: return
    if len(playerHand[target]) < count: count = len(playerHand[target])
    for i in range(0,count):
        cardIndex = selectFromHand(type,target)
        discardSelected(cardIndex,target)
    return

def selectFromHand(type=cardType.Any,target=activePlayer) -> int:
    try:
        index = int(input()) #TODO
    except type != playerHand[target][index]:
        selectFromHand(type,target)
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
