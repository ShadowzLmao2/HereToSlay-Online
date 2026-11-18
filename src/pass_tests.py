from strings import *
from config import *
from cards import *
from main import *

sys.dont_write_bytecode = True
#ranked = True
playerCount = 4
'''
All Mandatory Tests
    Must be passed before pushing to main

Categories:
- Game Mechanics
- Game Wins
- Card Effects (Leader, Hero, Magic, Item, Challenge)
- Monster Effects

Other Potential Categories - Inputs, End of Turn effects
'''
def runAllTests() -> bool:
    allTestsPassed: bool = False
    for i in range(0,100):
        #if not ...
            #allTestsPassed = False
            #whichFailed.append()
            #print(f"\033[91m {i} has failed")
        #else:
            #print(f"\033[92m {i} has succeeded")
        pass

    if not allTestsPassed: 
        color = '\033[91m'
    else: color = '\033[92m'
    return allTestsPassed, color

result, color = runAllTests()
print(f"{color}{result}")

#Game Mechanic Tests
'''
All Mechanic Tests
Start of Game
Start of Turn
    Randomness in coin flip, dice/die roll, and shuffle
End of Turn
Choose Leaders
Activated Hero/Leader Abilities
Leader and Hero Class (after changes)
Leader Type Switch
Unstable Unicorn (what a headache)
All dice roll modifiers
All inputs (End, Draw, Redraw, Attack, Activate Hero, Activate Leader, Play Card)
Play From Hand (Hero, Magic, Item)
Force Play Cards (Hero, Magic, Item)
Trade (Hero, Item)
Check For Modifiers and use modifier
Check Hand for a card
Pull a Card
Search Discard
Reveal Card
Look at a Player's Hand
Mill Cards
Destroy
Sacrifice (Hero, Item)
Steal (Hero, Item)
Trade Hands
Trade Leaders
Force Discard (All, Specific)
Shuffle Cards (from Field, GY)
Draw Monster Card
Win the Game (3-4 Monsters, 5-7 Classes)
Discard Hand/Specific
Spend AP
'''