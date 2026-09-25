from card_images import *
from strings import *
from config import *
from cards import *
from functions import *
from main import *
#ranked = True
playerCount = 4

def testLeaderTypeSwap():
    playerLeaders[1] = "Brutal Bow"
    playerLeaders[2] = "Charismatic Song"
    playerLeaders[3] = "Raging Manticore"
    playerLeaders[4] = "Unstable Unicorn"

    startGame()
    #leaderTypeSwitch("Brutal Bow")
    return

def testGame():
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

testLeaderTypeSwap()
# summon(1,"Sharp Fox",1)
#print(playerParties[1["Hero"[1]]])
#testGame()