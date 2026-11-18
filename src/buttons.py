from main import *
def fieldHero(index):
    if testingPhase:
        print(playerParties[activePlayer.current()[index]], "ability activated.")
    activateHeroAbility(playerParties[activePlayer.current()[index]])
    return