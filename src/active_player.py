from cards import *
from config import *
global activePlayer
global playerCount
monstersSlain = [0,0,0,0,0,0]
activeMonster = [0,0,0]
activatePlayer = 1
playerCount = 4 #Max = 6
discardPile = []
playerHand = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : []
}
monsterField = [0,0,0]
playerLeaders = {
    1 : Leaders["None"],
    2 : Leaders["None"],
    3 : Leaders["None"],
    4 : Leaders["None"],
    5 : Leaders["None"],
    6 : Leaders["None"],
}
playerParties = {
    1 : {
        #Front Row
        "Hero" : {
            1: Cards["None"],
            "1 Active" : False,
            2: Cards["None"],
            "2 Active" : False,
            3: Cards["None"],
            "3 Active" : False,
            4: Cards["None"],
            "4 Active" : False,
            5: Cards["None"],
            "5 Active" : False,
            6: Cards["None"],
            "6 Active" : False,
            7: Cards["None"],
            "7 Active" : False,
            },
        #Back Row
        "Monster" : {
            1: Monsters["None"],
            "1 Active" : False,
            2: Monsters["None"],
            "2 Active" : False,
            3: Monsters["None"],
            "3 Active" : False,
            },
        "Banner"  : {
            1: Banners["None"],
            "1 Active" : False,
            2: Banners["None"],
            "2 Active" : False,
            3: Banners["None"],
            "3 Active" : False,
            4: Banners["None"],
            "4 Active" : False,
            },
    },
    2 : {
        #Front Row
        "Hero" : {
            1: Cards["None"],
            "1 Active" : False,
            2: Cards["None"],
            "2 Active" : False,
            3: Cards["None"],
            "3 Active" : False,
            4: Cards["None"],
            "4 Active" : False,
            5: Cards["None"],
            "5 Active" : False,
            6: Cards["None"],
            "6 Active" : False,
            7: Cards["None"],
            "7 Active" : False,
            },
        #Back Row
        "Monster" : {
            1: Monsters["None"],
            "1 Active" : False,
            2: Monsters["None"],
            "2 Active" : False,
            3: Monsters["None"],
            "3 Active" : False,
            },
        "Banner"  : {
            1: Banners["None"],
            "1 Active" : False,
            2: Banners["None"],
            "2 Active" : False,
            3: Banners["None"],
            "3 Active" : False,
            4: Banners["None"],
            "4 Active" : False,
            },
    },
    3 : {
        #Front Row
        "Hero" : {
            1: Cards["None"],
            "1 Active" : False,
            2: Cards["None"],
            "2 Active" : False,
            3: Cards["None"],
            "3 Active" : False,
            4: Cards["None"],
            "4 Active" : False,
            5: Cards["None"],
            "5 Active" : False,
            6: Cards["None"],
            "6 Active" : False,
            7: Cards["None"],
            "7 Active" : False,
            },
        #Back Row
        "Monster" : {
            1: Monsters["None"],
            "1 Active" : False,
            2: Monsters["None"],
            "2 Active" : False,
            3: Monsters["None"],
            "3 Active" : False,
            },
        "Banner"  : {
            1: Banners["None"],
            "1 Active" : False,
            2: Banners["None"],
            "2 Active" : False,
            3: Banners["None"],
            "3 Active" : False,
            4: Banners["None"],
            "4 Active" : False,
            },
    },
    4 : {
        #Front Row
        "Hero" : {
            1: Cards["None"],
            "1 Active" : False,
            2: Cards["None"],
            "2 Active" : False,
            3: Cards["None"],
            "3 Active" : False,
            4: Cards["None"],
            "4 Active" : False,
            5: Cards["None"],
            "5 Active" : False,
            6: Cards["None"],
            "6 Active" : False,
            7: Cards["None"],
            "7 Active" : False,
            },
        #Back Row
        "Monster" : {
            1: Monsters["None"],
            "1 Active" : False,
            2: Monsters["None"],
            "2 Active" : False,
            3: Monsters["None"],
            "3 Active" : False,
            },
        "Banner"  : {
            1: Banners["None"],
            "1 Active" : False,
            2: Banners["None"],
            "2 Active" : False,
            3: Banners["None"],
            "3 Active" : False,
            4: Banners["None"],
            "4 Active" : False,
            },
    },
    5 : {
        #Front Row
        "Hero" : {
            1: Cards["None"],
            "1 Active" : False,
            2: Cards["None"],
            "2 Active" : False,
            3: Cards["None"],
            "3 Active" : False,
            4: Cards["None"],
            "4 Active" : False,
            5: Cards["None"],
            "5 Active" : False,
            6: Cards["None"],
            "6 Active" : False,
            7: Cards["None"],
            "7 Active" : False,
            },
        #Back Row
        "Monster" : {
            1: Monsters["None"],
            "1 Active" : False,
            2: Monsters["None"],
            "2 Active" : False,
            3: Monsters["None"],
            "3 Active" : False,
            },
        "Banner"  : {
            1: Banners["None"],
            "1 Active" : False,
            2: Banners["None"],
            "2 Active" : False,
            3: Banners["None"],
            "3 Active" : False,
            4: Banners["None"],
            "4 Active" : False,
            },
    },
    6 : {
        #Front Row
        "Hero" : {
            1: Cards["None"],
            "1 Active" : False,
            2: Cards["None"],
            "2 Active" : False,
            3: Cards["None"],
            "3 Active" : False,
            4: Cards["None"],
            "4 Active" : False,
            5: Cards["None"],
            "5 Active" : False,
            6: Cards["None"],
            "6 Active" : False,
            7: Cards["None"],
            "7 Active" : False,
            },
        #Back Row
        "Monster" : {
            1: Monsters["None"],
            "1 Active" : False,
            2: Monsters["None"],
            "2 Active" : False,
            3: Monsters["None"],
            "3 Active" : False,
            },
        "Banner"  : {
            1: Banners["None"],
            "1 Active" : False,
            2: Banners["None"],
            "2 Active" : False,
            3: Banners["None"],
            "3 Active" : False,
            4: Banners["None"],
            "4 Active" : False,
            },
    },
}