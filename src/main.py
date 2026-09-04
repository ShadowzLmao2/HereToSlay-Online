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
#Separate from the GUI, handles the main game once you enter a game with another player
def startGame():
    if testingPhase:
        print("PreGame Phase initialized")
    #pickLeaders()
    if ranked:
        shuffleDeck(rankedMonsterDeck)
        shuffleDeck(p1Deck)
        shuffleDeck(p2Deck)
        #drawCard(player1).drawCard(player1).drawCard(player1).drawCard(player1).drawCard(player1)
        #drawCard(player2).drawCard(player2).drawCard(player2).drawCard(player2).drawCard(player2)
        global playerCount, HereToSleigh
        playerCount = 2
        HereToSleigh = False
        #Start the first player's turn, determine who goes first
        #For ranked, run a coin flip. For all other modes, every player rolls the dice and highest roller goes first, then in clockwise.
        firstPlayer = flipCoin()
        drawCard(5,1)
        drawCard(5,2)

    else:        
        if testingPhase:
            print("mainDeck")
        shuffleDeck(mainDeck)
        if testingPhase:
            print("monsterDeck")
        shuffleDeck(monsterDeck)
        chooseLeader()
        for player in range (1,playerCount+1,1):
            drawCard(5,player)
    if testingPhase:
        print("PreGame Phase finalized")
    main()
    return

def main():
    if testingPhase:
        print("Player", activePlayer, "Turn initialized")
    startTurn(activePlayer)
    chooseAction()
    return

def startTurn(player):
    leader = playerLeaders[activePlayer]
    if testingPhase:
        print(leader["Start of Turn"])
    if (leader["Start of Turn"]):
        leaderTypeSwitch(playerLeaders[activePlayer])
    return

def chooseLeader():
    for i in range(1, playerCount+1):
        if testingPhase:
            print("Player", i)
        
    return
    
def leaderTypeSwitch(leader):
    confirmationBox(switchLeaderType)
    match leader:
        case "Brutal Bow":
            #Fighter/Ranger
            return
        case "Mystical Maestro":
            #Mage/Bard
            return
        case "Veiled Raider":
            #Guardian/Thief
            return
        case "Unstable Unicorn":
            #Copy another Leader
            return
        case "Fierce Panguardian":
            #Guardian/Fighter
            return
        case "Illusive Trickster":
            #Wizard/Thief
            return
        case "Rhythmic Archer":
            #Bard/Ranger
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
    #Working: endTurn()
    #WIP: activateHeroAbility(hero)
    #Not Working: draw() attack() discardDraw() endTurn() activateLeaderAbility(playerParties[activePlayer["Leader"]])
    endTurn()
    return

def activateHeroAbility(hero):
    if AP > 0:
        reduceAP(1)
        useHeroAbility(hero)
    else:
        print("No AP")
    
    return

def activateLeaderAbility(leader):
    if AP > 0 and Leaders[leader["Activatable"]]:
        reduceAP(1)
        useLeaderAbility(leader)
    else:
        print("No AP or no ability")
    return

global leaderAbilityUsed 
leaderAbilityUsed= False

def useLeaderAbility(leader):
    if leaderAbilityUsed:
        return 
    match Leaders[leader["Effect"]]:
        case heroEffect.ShadowClaw:
            playerIndex = chooseToPull()
            pullCard(playerIndex, False, 0)
            leaderAbilityUsed = True
            return
        case heroEffect.GnawingDread:
            index = searchDiscard(cardType.Any)
            reduceAP(2)
            playerHand[activePlayer].append(discardPile[index].pop())
            leaderAbilityUsed = True
            return
        case heroEffect.IllusiveTrickster:
            if checkHand(cardType.Magic, activePlayer):
                discardSpecfic(cardType.Magic)
                reduceAP(1)
                drawCard(activePlayer)
                drawCard(activePlayer)
                drawCard(activePlayer)
                leaderAbilityUsed = True
            else:
                return
            return
    return

def useHeroAbility(hero):
    match Cards[hero["Effect"]]:
        case cardEffect.FuzzyCheeks:
            drawCard(activePlayer)
            playCard(cardType.Hero,False)
            return
        #case cardEffect.:
        #    return
        #case cardEffect.:
        #    return
        #case cardEffect.:
        #    return
        #case cardEffect.:
        #    return
        #case cardEffect.:
        #    return
    return

def summonHero(slot,hero,player):
    global AP
    if AP > 0 and checkHeroSlot(slot,player):
        reduceAP(1)
        challenge()
        summon(slot,hero,player)
    return

def summon(slot,hero,player):
    playerParties[player["Hero"[slot]]] = Cards[hero]
    return
def checkHeroSlot(slot,player):
    if playerParties[player["Hero"[slot]]] == Cards["None"]:
        return False
    return True
def askPlayer():
    return
def challenge():
    return hasCardEffect(cardEffect.Challenge)
def hasCardEffect(effect):
    return
def chooseToPull():
    return
def pullCard(player,req,reqType):
    return
def searchDiscard(cardType):
    return
def playCard(cardType,optional):
    if checkHand(cardType, activePlayer):
        if optional:
            if askPlayer() == False:
                placeCard()
                removeCard()
                return
    else:
        placeCard()
        removeCard()
    return

def removeCard():
    return
def placeCard():
    return

def checkHand(ct, player):
    for card in playerHand[player]:
        if Cards[(playerHand[player[card]])["Card Type"]] == ct:
            return True
    return False
def handSize():
    return
def viewHand(player):
    return
def mill(numMilled):
    #mainDeck
    return
def destroy(target,player):
    discardPile.append(target)
    #playerParties[player["Hero"[target]]] = 0
    return
def sacrifice(target):
    return
def choosePlayer():
    return
def steal():
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

def doNothing():
    return
def protectionStatus(player):
    return

def draw():
    if AP > 0:
        reduceAP(1)
        drawCard(activePlayer)
    else:
        print("No AP")
    return

def drawCard(count, player):
    for i in range(0,count,1):
        playerHand[player].append(mainDeck.pop())
        if testingPhase:
            print("Player", player, "drew a card")
    if testingPhase:
        print(playerHand[player])
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
        effect = Monsters[monster["Win Effect"]]
    else:
        effect = Monsters[monster["Lose Effect"]]
    if effect == monsterRollEffect.slay:
        if monstersSlain[activePlayer] < 3:
            playerParties[activePlayer["Monster"[monstersSlain[activePlayer]]]] = Monsters[monster]
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
    drawCard(activePlayer)
    drawCard(activePlayer)
    drawCard(activePlayer)
    drawCard(activePlayer)
    drawCard(activePlayer)
    return

def discardSpecfic(type):
    cardIndex = selectFromHand(type)
    discardSelected(cardIndex)
    return

def selectFromHand(type):
    index = 0 #TODO
    return index

def discardSelected(cardIndex):
    discardPile.append(playerHand[activePlayer[cardIndex]].pop())
    return
def reduceAP(APReduction):
    global AP
    AP -= APReduction
    print(AP)
    return

def endTurn():
    global leaderAbilityUsed
    leaderAbilityUsed = False
    global AP, activePlayer, playerCount
    if testingPhase:
        print("End Phase of Player ", activePlayer, " initialized")
    if activePlayer == playerCount:
        activePlayer = 1
    else:
        activePlayer +=1
    AP = 3
    return

#startGame()