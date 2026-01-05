from config import *
from cards import *
from active_player import *
import random
global AP
AP = 3
def startGame():
    #pickLeaders()
    shuffleDeck()
    #draw(4,all)
    return
def main():
    chooseAction()
    return

def shuffleDeck():
    #Main
    for i in range(len(mainDeck)-1,0,-1):
        r = random.randint(0,i)
        mainDeck[i], mainDeck[r] = mainDeck[r], mainDeck[i]
    #Monster
    for i in range(len(monsterDeck)-1,0,-1):
        r = random.randint(0,i)
        monsterDeck[i], monsterDeck[r] = monsterDeck[r], monsterDeck[i]
    #print("Main ",mainDeck)
    #print("Monster ",monsterDeck)
    return

def chooseAction():
    #draw() activateHeroAbility() attack() discardDraw() endTurn()
    activateLeaderAbility(Leaders["Charismatic Song"])
    return

def activateHeroAbility():
    if checkAP() > 0:
        reduceAP(1)
    else:
        print("No AP")
    return

def activateLeaderAbility(leader):
    if checkAP() > 0 and Leaders[leader["Activatable"]]:
        reduceAP(1)
        useLeaderAbility(leader)
    else:
        print("No AP or no ability")
    return

def useLeaderAbility(leader):
    match Leaders[leader["Effect"]]:
        case cardEffect.ShadowClaw:
            pullCard()
            return
        case cardEffect.GnawingDread:
            searchDiscard(cardType.Any)
            return
    return

def useHeroAbility(hero):
    match Heroes[hero["Effect"]]:
        case cardEffect.FuzzyCheeks:
            drawCard()
            playCard(cardType.Hero,False)
            return
    return

def summonHero(slot,hero,player):
    if checkAP() > 0 and checkHeroSlot(slot,player):
        reduceAP(1)
        challenge()
        summon(slot,hero,player)
    return

def summon(slot,hero,player):
    playerParties[player["Hero"[slot]]] = Heroes[hero]
    return
def checkHeroSlot(slot,player):
    if playerParties[player["Hero"[slot]]] == Heroes["None"]:
        return False
    return True
def askPlayer():
    return
def challenge():
    return hasCardEffect(cardEffect.Challenge)
def hasCardEffect(effect):
    return
def pullCard(player,req,reqType):
    return
def searchDiscard(cardType):
    return
def playCard(cardType,optional):
    if checkHand(cardType):
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

def checkHand(cardType):
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
    if checkAP() > 0:
        reduceAP(1)
        drawCard(activePlayer)
    else:
        print("No AP")
    return

def drawCard(player):
    playerHand[player].append(mainDeck.pop())
    #print(playerHand)
    return

def attack():
    if checkAP() > 0:
        reduceAP(2)
    else:
        print("Not enough AP")
    return

def discardHand():
    for card in len(playerHand[activePlayer]):
        discardPile.append(playerHand[activePlayer].pop)
    return

def discardDraw():
    if checkAP() > 0:
        reduceAP(3)
    else:
        print("Not enough AP")
        return
    discardHand()
    drawCard(activePlayer).drawCard(activePlayer).drawCard(activePlayer).drawCard(activePlayer).drawCard(activePlayer)
    return

def checkAP():
    return AP

def reduceAP(APReduction):
    global AP
    AP -= APReduction
    print(AP)
    return

def endTurn():
    global AP
    global activePlayer
    global maxPlayers
    AP = 3
    if activePlayer == maxPlayers:
        activePlayer = 1
    else:
        activePlayer +=1
    return
