from main import *
def fieldHero(index):
    if testingPhase:
        print(playerHeroes[activePlayer.current()][index], "ability activated.")
    activateHeroAbility(index)
    return