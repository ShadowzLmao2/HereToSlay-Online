from cards import *
#from card_images import *
#from config import *
leaderAbilityUsed = False
heroAbilityUsed: bool = []
discardPile = []

class activePlayerClass:
    activePlayer = 1
    playerCount = 2
    def __init__(self):
        pass

    @classmethod
    def playerCount(cls, playerCount: int):
        cls.playerCount = playerCount
        if testingPhase:
            print(f"Player Count: {playerCount}")

    @classmethod
    def increment(cls):
        if testingPhase:
            print(f"Before: {cls.activePlayer}")
        if cls.activePlayer == cls.playerCount:
            cls.activePlayer = 1
        else:
            cls.activePlayer += 1
        if testingPhase:
            print(f"After: {cls.activePlayer}")

    @classmethod
    def current(cls):
        return cls.activePlayer

    @classmethod
    def count(cls):
        return cls.playerCount


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