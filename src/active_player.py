from cards import *
#from card_images import *
#from config import *
leaderAbilityUsed = False
heroAbilityUsed: bool = []
discardPile = []

class activePlayerClass:
    activePlayer = 1
    def __init__(self,playerCount):
        self.playerCount = playerCount

    def updatePlayerCount(self,playerCount):
        self.playerCount = playerCount

    def increment(self):
        cls = type(self)
        if testingPhase:
            print(f"Before: {cls.activePlayer}")
        if cls.activePlayer == self.playerCount:
            cls.activePlayer = 1
        else:
            cls.activePlayer += 1
        if testingPhase:
            print(f"After: {cls.activePlayer}")

    @classmethod
    def current(cls):
        return cls.activePlayer

    def count(self):
        return self.playerCount


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