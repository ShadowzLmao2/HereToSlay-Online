from card_images import *
from strings import *
from config import *
from cards import *
from functions import *
from main import *
#ranked = True
playerCount = 6



def testLeaderTypeSwap():

    leaderTypeSwitch("Brutal Bow")
    return



def testGame():
    startGame()
    return
'''  Game Order
PreGame Phase      - "PreGame Phase initialized"
Deck Shuffle Phase - the deck name is printed and then the deck
Draw Phase         - Player # is printed, and then their hand, monster cards drawn are printed
Player Turn Phase  - Player # is printed and their turn is started. Currently, the turn ends right away
'''


#What you want to test (comment out all other test functions):

#print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

#testLeaderTypeSwap()
playerLeaders[1] = "Brutal Bow"
summon(1,"Sharp Fox",1)
#print(playerParties[1["Hero"[1]]])
#print(playerLeaders[1])
#print(Leaders[(playerLeaders[1])])
#testGame()