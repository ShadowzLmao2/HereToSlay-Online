from cards import *
global AP
def main():
    chooseAction()
    return

def chooseAction():
    #draw() activateLeaderAbility() activateHeroAbility() attack() discardDraw()
    return

def activateHeroAbility():
    if checkAP() > 0:
        reduceAP(1)
    else:
        print("No AP")
    return

def activateLeaderAbility():
    if checkAP() > 0:
        reduceAP(1)
    else:
        print("No AP")
    return

def draw():
    if checkAP() > 0:
        reduceAP(1)
    else:
        print("No AP")
    return

def drawCard():
    return

def attack():
    if checkAP() > 0:
        reduceAP(2)
    else:
        print("Not enough AP")
    return

def discardHand():
    return

def discardDraw():
    if checkAP() > 0:
        reduceAP(3)
    else:
        print("Not enough AP")
    discardHand()
    drawCard()
    drawCard()
    drawCard()
    drawCard()
    drawCard()
    return

def checkAP():
    return AP

def reduceAP(APReduction):
    AP -= APReduction
    print(AP)
    return

reduceAP(2)