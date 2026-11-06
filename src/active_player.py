from cards import *
#from card_images import *
#from config import *
activatedHeroAbility: bool = []
activatePlayer = 1
playerCount = 4 #Max = 6
discardPile = []
playerEffects = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
majestelk = False
playerHand = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

monsterField = ["None","None","None"]
leaderCurrentType = {
    1 : heroClass.NoClass,
    2 : heroClass.NoClass,
    3 : heroClass.NoClass,
    4 : heroClass.NoClass,
    5 : heroClass.NoClass,
    6 : heroClass.NoClass
}
playerLeaders = {
    1 : "None",
    2 : "None",
    3 : "None",
    4 : "None",
    5 : "None",
    6 : "None"
}
unstableUnicornTarget = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6
}
playerMonsters = [[],
                  [],
                  [],
                  [],
                  [],
                  [],
                  []]

playerHeroes = [[],
                [],
                [],
                [],
                [],
                [],
                []]

heroItems = [[],
             [],
             [],
             [],
             [],
             [],
             []]

morphMaskType = [[],
             [],
             [],
             [],
             [],
             [],
             []]
playerBanners = [[],
                 [],
                 [],
                 [],
                 [],
                 [],
                 []]