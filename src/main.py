from config import *
from cards import *
from active_player import *
from tutorial import *
from functions import *
from strings import *
import random
#from enum import Enum
global AP
AP = 3
activePlayer = 1
turnCount = 1
playerCount = 4

#Separate from the GUI, handles the main game once you enter a game with another player
def startGame() -> None:
    if testingPhase:
        print("\n________________________________________________________________________________________________________________________________________________________________________________________________________________")
        print("PreGame Phase started\n")
    #pickLeaders()
    if testingPhase:
        print("\nMonster Deck:")
    random.shuffle(monsterDeck)
    drawMonsterCard(3)
    if ranked:
        random.shuffle(p1Deck)
        random.shuffle(p2Deck)
        drawCard(5,1)
        drawCard(5,2)
        global playerCount
        playerCount = 2
        #Start the first player's turn, determine who goes first
        #For ranked, run a coin flip. For all other modes, every player rolls the dice and highest roller goes first, then in clockwise.
        global activePlayer
        activePlayer = flipCoin()+1
    else:        
        if testingPhase:
            print("Main Deck:")
        random.shuffle()
        chooseLeader()
        for player in range(1,playerCount+1,1):
            drawCard(5,player)
    if testingPhase:
        print("PreGame Phase finished")
        print("\n________________________________________________________________________________________________________________________________________________________________________________________________________________")
    main()
    return

#Runs every round after startGame has been activated once and ends with endTurn()
def main() -> None:
    if testingPhase:
        print(f"Player {activePlayer} turn started")
    startTurn() 
    chooseAction() #Basically waits for input
    return

#All the "Standby Phase" Stuff
def startTurn(player=activePlayer) -> None:
    if testingPhase:
        print("Turn Number:", turnCount)
        #if turnCount > 1:
            #print(f"Start of turn effect: {playerLeaders[activePlayer]["Start of Turn"]}")
    if (Leaders[playerLeaders[activePlayer]]["Start of Turn"] and turnCount != 0): #Only for the KickStarter leaders and Individual Exclusive leaders
        leaderTypeSwitch()
        if testingPhase:
            print(f"{playerLeaders[activePlayer]}: {playerLeaderCurrentType[activePlayer]}")
    return

def chooseLeader() -> None: #Pick your leader at the start of the game. Only used in casual
    if testingPhase:
        print("     Leader Section:\n")
    global playerCount
    for i in range(1, playerCount+1,1):
        playerLeaderCurrentType[i] = Leaders[(playerLeaders[i])]["Class"]
        if testingPhase:
            print(f"Player {i}: {playerLeaders[i]}, Class: {playerLeaderCurrentType[i]}")
    return

#For the KSE/IE leaders, asks player if they want to switch types, then switches if they say yes
def leaderTypeSwitch(leader=playerLeaders[activePlayer]) -> None:
    if input(f"{switchLeaderType}\n") == "y":
        leaderType = playerLeaderCurrentType[activePlayer]
        match leader:
            case "Brutal Bow":
                #Fighter/Ranger
                if leaderType == heroType.Fighter:
                    playerLeaderCurrentType[activePlayer] = heroType.Ranger
                else:
                    playerLeaderCurrentType[activePlayer] = heroType.Fighter
                return
            case "Mystical Maestro":
                #Wizard/Bard
                if leaderType == heroType.Wizard:
                    playerLeaderCurrentType[activePlayer] = heroType.Bard
                else:
                    playerLeaderCurrentType[activePlayer] = heroType.Wizard
                return
            case "Veiled Raider":
                #Guardian/Thief
                if leaderType == heroType.Guardian:
                    playerLeaderCurrentType[activePlayer] = heroType.Thief
                else:
                    playerLeaderCurrentType[activePlayer] = heroType.Guardian
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
                    playerLeaderCurrentType[activePlayer] = heroType.Fighter
                else:
                    playerLeaderCurrentType[activePlayer] = heroType.Guardian
                return
            case "Illusive Trickster":
                #Wizard/Thief
                if leaderType == heroType.Wizard:
                    playerLeaderCurrentType[activePlayer] = heroType.Thief
                else:
                    playerLeaderCurrentType[activePlayer] = heroType.Wizard
                return
            case "Rhythmic Archer":
                #Bard/Ranger
                if leaderType == heroType.Bard:
                    playerLeaderCurrentType[activePlayer] = heroType.Ranger
                else:
                    playerLeaderCurrentType[activePlayer] = heroType.Bard
                return
    return

def flipCoin() -> int:
    #0 = Tails, 1 = Heads
    coinFlip = random.int(0,1)
    return coinFlip

def rollDice() -> int:
    return random.int(1,6) + random.int(1,6)

def chooseAction() -> None:
    #Working: endTurn() draw() discardDraw() 
    #WIP: activateHeroAbility(hero) activateLeaderAbility(leader)
    #Not Working: attack() 
    endTurn()
    return

def activateHeroAbility(hero) -> None:
    if AP > 0:
        reduceAP()
        diceRoll = rollDice()
        #TODO Unstable Unicorn Stuff
        if playerLeaders[activePlayer] == "Charismatic Song":
            diceRoll +=1
        if  diceRoll >= Cards[hero]["Effect Roll"]:
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
    global leaderAbilityUsed
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
    global AP
    if AP > 0 and checkHeroSlot(slot,player,"None"):
        reduceAP()
        challenge()
        summon(slot,hero,player)
    return

def summon(slot,hero,player=activePlayer) -> None:
    playerParties[player]["Hero"][slot] = hero
    return

def checkHeroSlot(slot,player,key) -> bool:
    return playerParties[player]["Hero"][slot] == key

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
    return

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

def destroy(target,player) -> None:
    discardPile.append(target)
    playerParties[player]["Hero"][target] = "None"
    #TODO effects that happen after destroyed 
    if playerLeaders[activePlayer] == "Brutal Bow":
        drawCard(1)
    return

def sacrifice(target) -> None:
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
    if AP > 1:
        reduceAP(2)
    else:
        print("Not enough AP")
        return
    monster = selectMonster()
    heroReq = checkAtkRequirements(monster)
    diceRoll = rollDice()
    if playerLeaders[activePlayer] == "Divine Arrow":
        diceRoll +=1
    if diceRoll >= Monsters[monster]:
        effect = Monsters[monster]["Win Effect"]
    else:
        effect = Monsters[monster]["Lose Effect"]
    if effect == monsterRollEffect.slay:
        if monstersSlain[activePlayer] < 3:
            playerParties[activePlayer]["Monster"][monstersSlain][activePlayer] = Monsters[monster]
            monstersSlain[activePlayer]  += 1
            activeMonster[monster] = monsterDeck.pop()
            if playerLeaders[activePlayer] == "Raging Manticore":
                drawCard(2)
        else:
            endGame()
    else:
        #Should activate on any player's fail
        if playerLeaders[activePlayer] == "Rhythmic Archer":
            drawCard(1)
    return

def endGame() -> None:
    return

def selectMonster() -> int:
    return 0

def checkAtkRequirements(monster):
    activeMonster[monster]
    heroReq = 0
    return

def discardHand() -> None:
    if not playerHand[activePlayer]: return #Return if empty
    for card in len(playerHand[activePlayer]):
        discardPile.append(playerHand[activePlayer].pop())
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

def reduceAP(APReduction=1) -> None:
    global AP
    AP -= APReduction
    if testingPhase:
        print(f"AP: {AP}")
    return

def endTurn() -> None:
    global leaderAbilityUsed
    leaderAbilityUsed = False
    global AP, activePlayer, playerCount, turnCount
    if testingPhase:
        print(f"Player {activePlayer} End Phase started")
    if activePlayer == playerCount:
        activePlayer = 1
    else:
        activePlayer +=1
    AP = 3
    turnCount +=1
    return

#Stores the x and y values of a button, as when a button is hidden it loses said values
class position:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
