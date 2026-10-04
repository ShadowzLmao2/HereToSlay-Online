from card_images import *
from strings import *
from config import *
from cards import *
from functions import *
from main import *
import random as rand
#ranked = True
playerCount = 4

def testPullCard() -> None:
    playerHand[2].append("Bear Claw")
    print(f"Initial Hands: {playerHand[1]}, {playerHand[2]}")
    correctPullType = pullCard(2,heroType.Fighter)
    print(f"Final Hands: {playerHand[1]}, {playerHand[2]}")
    print(f"Was it a fighter? {correctPullType}")
    return

def testLeaderTypeSwap() -> None:
    global playerCount
    playerCount = 3
    playerLeaders[1] = "Brutal Bow"       #Leader that can switch types
    playerLeaders[2] = "Charismatic Song" #Leader that can't
    playerLeaders[3] = "Unstable Unicorn" #Unicorn Effect

    startGame()
    #leaderTypeSwitch("Brutal Bow")
    return

def checkCardsInHand() -> None:
    #If the hand is empty
    if not playerHand[1]:
        print("Empty")

    playerHand[1].append("Mirroryu")
    playerHand[1].append("Luut")
    #Random index in hand
    index = rand.randint(0,len(playerHand[1])-1)
    print(f"Random index: {index}")
    print(f"Hand Size: {len(playerHand[1])}")
    #print(f"Card: {playerHand[1]}")
    return

def printAllHeroes():
    for i, key in enumerate(Cards):
        if Cards[list(Cards)[i]]["Card Type"] == cardType.Hero:
            print(f"\"{key}\"")
    return

def testGame() -> None:
    startGame()
    return
'''  Game Order
PreGame Phase      - "PreGame Phase initialized"
    Deck Shuffle Phase - the deck name is printed and then the deck
    Leader Phase       - All players pick leaders and the leaders are printed
    Draw Phase         - Player # is printed, and then their hand, monster cards drawn are printed
Player Turn Phase  - Player # is printed and their turn is started. Currently, the turn ends right away
'''

#What you want to test (comment out all other test functions):
#print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

for i in range(0,len(rankedMonsterBanlist)):
    monsterDeck.remove(rankedMonsterBanlist[i])
#printAllHeroes()
#testPullCard()
#checkCardsInHand()
#testLeaderTypeSwap()
#testGame()