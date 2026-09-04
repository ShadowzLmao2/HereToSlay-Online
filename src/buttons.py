from main import *
def fieldHero(index):
    if testingPhase:
        print(playerParties[activePlayer[index]], "ability activated.")
    activateHeroAbility(playerParties[activePlayer[index]])
    return