from cards import *
#from card_images import *
#from config import *
leaderAbilityUsed = False
heroAbilityUsed: bool = []
discardPile = []

class activePlayerClass:
    def __init__(self,playerCount: int,activePlayer: int = 1):
        self.activePlayer = activePlayer
        self.playerCount = playerCount
        self.gameEnded = False

    def updatePlayerCount(self,playerCount):
        self.playerCount = playerCount

    def increment(self):
        if testingPhase:
            print(f"Before: {self.activePlayer}")
        if self.activePlayer == self.playerCount:
            self.activePlayer = 1
        else:
            self.activePlayer += 1
        if testingPhase:
            print(f"After: {self.activePlayer}")

    def current(self):
        return self.activePlayer

    def count(self):
        return self.playerCount

    def isGameDone(self):
        return self.gameEnded
    
    def endGame(self):
        self.gameEnded = True


playerEffects = [
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

maskClass = [[],
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