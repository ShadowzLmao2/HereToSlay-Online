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

def testBanlist() -> None:
    for i in range(0,len(rankedMonsterBanlist)):
        monsterDeck.remove(rankedMonsterBanlist[i])
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

def discardHandTest():
    playerHand[1].append("Mirroryu")
    playerHand[1].append("Extraga")
    print(f"Before: {playerHand[1]}")
    discardHand()
    print(f"After: {playerHand[1]}")
    print(f"Discard Pile: {discardPile}")
    return

def testAttackReqCheck():
    test: str = input()
    monster: str = ""
    if test == "Hero Count":
        monster = "Chitin Scourge"
    elif test == "Class Req":
        monster = "Malamammoth"
        playerHeroes[1].append("Mirroryu")
        playerHeroes[1].append("Extraga")

    checkAtkRequirements(monster)
    return

def monsterDeckPopTest():
    #random.shuffle(monsterDeck)
    print(monsterDeck)
    monsterField[0] = monsterDeck.pop()
    monsterField[1] = monsterDeck.pop()
    monsterField[2] = monsterDeck.pop()
    print(monsterField)
    print(playerMonsters)
    for index in range(0,3):
        print(f"Round: {index+1}")
        playerMonsters[0].append(monsterField[index])
        monsterField[index] = monsterDeck.pop()
        print(f"Monster {index+1}: {playerMonsters[0]}")
        #print(f"Monsters: {monsterField}")
    print(playerMonsters)
    return

def testWin() -> None:
    print(testCommands)
    test: str = input("What are you testing: ")
    match test:
        case "Class":
            playerHeroes[1].append("Lucky Bucky")
            playerHeroes[1].append("Bad Axe")
            playerHeroes[1].append("Calming Voice")
            playerHeroes[1].append("Hook")
            playerHeroes[1].append("Shurikitty")
            playerHeroes[1].append("Bun Bun")
            startGame(test="testWin Class")
            return
        case "Monster":
            return
        case _:
            startGame(test)
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

#testAttackReqCheck()

#discardHandTest()
#printAllHeroes()
#testPullCard()
#checkCardsInHand()
#testLeaderTypeSwap()
#monsterDeckPopTest()
testWin() #Run testWin and dont give an input to just test the game