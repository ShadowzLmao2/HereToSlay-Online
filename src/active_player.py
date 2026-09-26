from cards import *
#from config import *
from card_images import *
monstersSlain = [0,0,0,0,0,0]
activeMonster = [0,0,0]
activatePlayer = 1
playerCount = 4 #Max = 6
discardPile = []
playerHand = {
    1 : {},
    2 : {},
    3 : {},
    4 : {},
    5 : {},
    6 : {}
}
monsterField = [0,0,0]
playerLeaderCurrentType = {
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
playerParties = {
    1 : {
        #Front Row
        "Hero" : {
            1: "None",
            2: "None",
            3: "None",
            4: "None",
            5: "None",
            6: "None",
            7: "None",
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
            1: "None",
            2: "None",
            3: "None",
            4: "None",
            5: "None",
            6: "None",
            7: "None",
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
            1: "None",
            2: "None",
            3: "None",
            4: "None",
            5: "None",
            6: "None",
            7: "None",
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
            1: "None",
            2: "None",
            3: "None",
            4: "None",
            5: "None",
            6: "None",
            7: "None",
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
            1: "None",
            2: "None",
            3: "None",
            4: "None",
            5: "None",
            6: "None",
            7: "None",
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
            1: "None",
            2: "None",
            3: "None",
            4: "None",
            5: "None",
            6: "None",
            7: "None",
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