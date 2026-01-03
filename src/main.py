from config import *
from cards import *
global AP
AP = 3
def main():
    chooseAction()
    return

def chooseAction():
    #draw()  activateHeroAbility() attack() discardDraw()
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
            playCard(cardType.Hero)
            return
    return

def pullCard():
    return
def searchDiscard(cardType):
    return
def playCard(cardType):
    return

def draw():
    if checkAP() > 0:
        reduceAP(1)
        drawCard()
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
    global AP
    AP -= APReduction
    print(AP)
    return

reduceAP(2)