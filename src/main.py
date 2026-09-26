from config import *
from cards import *
from active_player import *
from tutorial import *
from functions import *
from strings import *
import random as rand
#from enum import Enum
global AP
AP = 3
activePlayer = 1
turnCount = 1
playerCount = 4

#Separate from the GUI, handles the main game once you enter a game with another player
def startGame():
    if testingPhase:
        print("\n________________________________________________________________________________________________________________________________________________________________________________________________________________")
        print("PreGame Phase started\n")
    #pickLeaders()
    if ranked:
        shuffleDeck(rankedMonsterDeck)
        shuffleDeck(p1Deck)
        shuffleDeck(p2Deck)
        drawCard(5,1)
        drawCard(5,2)
        global playerCount
        playerCount = 2
        HereToSleigh = False
        #Start the first player's turn, determine who goes first
        #For ranked, run a coin flip. For all other modes, every player rolls the dice and highest roller goes first, then in clockwise.
        global activePlayer
        activePlayer = flipCoin()+1
    else:        
        if testingPhase:
            print("Main Deck:")
        shuffleDeck(mainDeck)
        if testingPhase:
            print("\nMonster Deck:")
        shuffleDeck(monsterDeck)
        chooseLeader()
        for player in range(1,playerCount+1,1):
            drawCard(5,player)
    drawMonsterCard(3)
    if testingPhase:
        print("PreGame Phase finished")
        print("\n________________________________________________________________________________________________________________________________________________________________________________________________________________")
    main()
    return

#Runs every round after startGame has been activated once and ends with endTurn()
def main():
    if testingPhase:
        print(f"Player {activePlayer} turn started")
    startTurn(activePlayer) 
    chooseAction() #Basically waits for input
    return

#All the "Standby Phase" Stuff
def startTurn(player):
    if testingPhase:
        print("Turn Number:", turnCount)
        if turnCount > 1:
            print(f"Start of turn effect: {playerLeaders[activePlayer]["Start of Turn"]}")
    if (Leaders[playerLeaders[activePlayer]]["Start of Turn"] and turnCount != 0): #Only for the KickStarter leaders and Individual Exclusive leaders
        leaderTypeSwitch(playerLeaders[activePlayer])
        if testingPhase:
            print(f"{playerLeaders[activePlayer]}: {playerLeaderCurrentType[activePlayer]}")
    return

def chooseLeader(): #Pick your leader at the start of the game. Only used in casual
    if testingPhase:
        print("     Leader Section:\n")
    global playerCount
    for i in range(1, playerCount+1,1):
        playerLeaderCurrentType[i] = Leaders[(playerLeaders[i])]["Class"]
        if testingPhase:
            print(f"Player {i}: {playerLeaders[i]}, Class: {playerLeaderCurrentType[i]}")
    return

#For the KSE/IE leaders, asks player if they want to switch types, then switches if they say yes
def leaderTypeSwitch(leader):
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
                    unstableUnicornTarget[activePlayer] = choosePlayer(0)
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

def flipCoin():
    #0 = Tails, 1 = Heads
    coinFlip = rand.int(0,1)
    return coinFlip
def rollDice():
    return rand.int(1,6)+rand.int(1,6)

def shuffleDeck(deck):
    #Main
    for i in range(len(deck)-1,0,-1):
        r = rand.randint(0,i)
        deck[i], deck[r] = deck[r], deck[i]
    
    if testingPhase:
        print(deck)
    return

def chooseAction():
    #Working: endTurn() draw() discardDraw() 
    #WIP: activateHeroAbility(hero) activateLeaderAbility(leader)
    #Not Working: attack() 
    endTurn()
    return

def activateHeroAbility(hero):
    if AP > 0:
        reduceAP(1)
        if rollDice() >= Cards[hero]["Effect Roll"]:
            useHeroAbility(hero)
        else:
            if testingPhase:
                print("Failed the roll")
    else:
        print("No AP")
    
    return

#Used for useLeaderAbility
leaderAbilityUsed= False

def activateLeaderAbility(leader):
    #Sets the Unicorn's ability to whatever it copied at the start of the turn
    if playerLeaders[activePlayer] == "Unstable Unicorn":
        leader = playerLeaders[(unstableUnicornTarget[activePlayer])]

    #Checks if it can be activated, if not return
    if AP >= Leaders[leader]["AP Cost"] and Leaders[leader]["Activatable"] and not leaderAbilityUsed:
        #Cost
        reduceAP(1)
        useLeaderAbility(leader)
    else:
        print("No AP or no ability")
    return

def useLeaderAbility(leader):
    global leaderAbilityUsed
    match Leaders[leader]["Effect"]:
        case leaderEffect.ShadowClaw:
            if ranked and ((activePlayer == 1 and not playerHand[2]) or (activePlayer == 2 and not playerHand[1])):
                return #No target
            elif ranked and activePlayer == 1: target = 2
            elif ranked and activePlayer == 2: target = 1
            else:
                target = choosePlayer(1)
            #Need to get a target in the hand. will do rand for now
            pullCard(target, False, 0)
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
                discardSpecific(cardType.Magic)
                drawCard(3,activePlayer)
                leaderAbilityUsed = True
            return
    return

def useHeroAbility(hero):
    match Cards[hero]["Effect"]:
        case cardEffect.BadAxe:
            player = choosePlayer(0)
            target = chooseHero()
            destroy(target, player)
            return
        case cardEffect.PullCard:
            target = choosePlayer(0)
            pulledCard = pullCard(target,False,0)
            if Cards[pulledCard]["Class"] == Cards[hero]["Pull Type"]:
                pullCard(target,False,0)
            return
        case cardEffect.BearyWise:
            allPlayersDiscard(False, cardType.Any)
            #TODO player picks a card from the discarded
            return
        case cardEffect.ForceDiscard:
            discardSpecific(choosePlayer(0),2)
            return
        case cardEffect.PanChucks:
            drawCard(2,activePlayer)
            firstDraw = playerHand[activePlayer][-2]
            secondDraw = playerHand[activePlayer][-1]
            if testingPhase:
                print("Drew", firstDraw, "and", secondDraw)
                if Cards[activePlayer][firstDraw]["Effect"] == cardEffect.Challenge:
                    revealCard(-2)
                    player = choosePlayer(0)
                    target = chooseHero()
                    destroy(target, player)
                if Cards[activePlayer][secondDraw]["Effect"] == cardEffect.Challenge:
                    revealCard(-1)
                    player = choosePlayer(0)
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
            drawCard(1,activePlayer)
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
            drawCard(2,activePlayer)
            return
        case cardEffect.SearchDiscard:
            searchDiscard(Cards[hero]["Search Target"])
            return
        case cardEffect.StealHero:
            stealHero()
            return
        case cardEffect.PullAndPlay:
            pullCard(choosePlayer(0),True,Cards[hero]["Search Target"])
            return
        case cardEffect.Play2:
            playCards(activePlayer,2,False,Cards[hero]["Search Target"])
            return
    return

def playCards(target,count,pickAll,type):
    for i in range(0,count,1):
        match(type):
            case cardType.Hero:
                return
            case cardType.Magic:
                return
            case cardType.Item:
                return
    return

def summonHero(slot,hero,player):
    global AP
    if AP > 0 and checkHeroSlot(slot,player,"None"):
        reduceAP(1)
        challenge()
        summon(slot,hero,player)
    return

def summon(slot,hero,player):

    playerParties[player]["Hero"][slot] = hero
    return

def checkHeroSlot(slot,player,key):
    if playerParties[player]["Hero"][slot] == key:
        return True
    return False

def askPlayer() -> bool:
    return

def choosePlayer(req) -> int:
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
    
def chooseHero(player):
    return

def challenge():
    return hasCardEffect(cardEffect.Challenge)

def hasCardEffect(effect):
    return

def pullCard(target,req,reqType) -> int:
    #target is who is stolen from, req is true/false for if there is a requirement, reqType is what card type you need to pull or else you dont pull
    pullIndex = int(rand(range(0,len(playerHand[target]))))
    
    playerHand[activePlayer].append()
    return #return the type

def searchDiscard(cardType):
    return

def playCard(cardType,optional):
    if checkHand(cardType, activePlayer):
        if optional:
            if askPlayer() == False:
                placeCard()
                removeFromHand()
                return
    else:
        whichCard(True,cardType)
        placeCard()
        removeFromHand()
    return

def revealCard(index):
    return

def whichCard(matchType,typeToMatch):
    return

def removeFromHand():
    return

def placeCard():
    return

def checkHand(cardType, player):
    for card in playerHand[player]:
        if Cards[(playerHand[player][card])]["Card Type"] == cardType:
            return True
    return False

def checkField():
    return

def handSize():
    return

def viewHand(player):
    return

def mill(numMilled):
    #mainDeck
    return

def destroy(target,player):
    discardPile.append(target)
    playerParties[player]["Hero"][target] = "None"
    #TODO effects that happen after destroyed 
    return

def sacrifice(target):
    return

def stealHero():
    return

def checkHeroItem():
    return

def giveCard():
    return

def tradeHands():
    return

def checkDrawn():
    return

def returnCard(cardType,target):
    return

def equipItem():
    return

def allPlayersDiscard(hitSelf, cardType):
    for i in range(1,playerCount+1):
        if hitSelf or i != activePlayer:
            discardSpecific(cardType,1)
    return

def doNothing():
    return

def protectionStatus(player):
    return

def draw():
    if AP > 0:
        reduceAP(1)
        drawCard(1,activePlayer)
    else:
        print("No AP")
    return

def drawCard(count, player):
    for i in range(0,count,1):
        playerHand[player].append(mainDeck.pop())
    if testingPhase:
        print(f"Player {player} drew {count} card(s)")
        print(playerHand[player])
    return

def drawMonsterCard(count):
    for i in range(2,2-count,-1):
        monsterField[i] = monsterDeck[-1]
        monsterDeck.pop()
    if testingPhase:
        print(f"{count} Monster Card(s) were/was drawn")
        print(monsterField)
    return

def attack():
    if AP > 1:
        reduceAP(2)
    else:
        print("Not enough AP")
        return
    monster = selectMonster()
    heroReq = checkAtkRequirements(monster)
    if rollDice() >= Monsters[monster]:
        effect = Monsters[monster]["Win Effect"]
    else:
        effect = Monsters[monster]["Lose Effect"]
    if effect == monsterRollEffect.slay:
        if monstersSlain[activePlayer] < 3:
            playerParties[activePlayer]["Monster"][monstersSlain][activePlayer] = Monsters[monster]
            monstersSlain[activePlayer]  += 1
            activeMonster[monster] = monsterDeck.pop()
        else:
            endGame()
    return

def endGame():
    return

def selectMonster():
    return 0

def checkAtkRequirements(monster):
    activeMonster[monster]
    heroReq = 0
    return

def discardHand():
    for card in len(playerHand[activePlayer]):
        discardPile.append(playerHand[activePlayer].pop())
    return

def discardDraw():
    if AP > 0:
        reduceAP(3)
    else:
        print("Not enough AP")
        return
    discardHand()
    drawCard(5,activePlayer)
    return

def discardSpecific(type,count,target):
    for i in range(0,count):
        cardIndex = selectFromHand(type,target)
        discardSelected(cardIndex,target)
    return

def selectFromHand(type,target):
    index = int(input()) #TODO
    return index

def discardSelected(cardIndex,target):
    discardPile.append(playerHand[target][cardIndex].pop())
    return

def reduceAP(APReduction):
    global AP
    AP -= APReduction
    print(AP)
    return

def endTurn():
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

#Make sure this is at the end
#startGame()