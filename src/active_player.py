from cards import *
#from config import *
from card_images import *
activatedHeroAbility: bool = []
activatePlayer = 1
playerCount = 4 #Max = 6
discardPile = []
playerHand = [
    [],
    [],
    [],
    [],
    [],
    []
]

monsterField = [0,0,0]
leaderCurrentType = {
    1 : heroType.NoClass,
    2 : heroType.NoClass,
    3 : heroType.NoClass,
    4 : heroType.NoClass,
    5 : heroType.NoClass,
    6 : heroType.NoClass
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
                  []]

playerHeroes = [[],
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
             []]

playerBanners = [[],
                [],
                [],
                [],
                [],
                []]