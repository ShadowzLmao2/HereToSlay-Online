from enum import Enum
class cardEffect(Enum):
    NoEffect = 0
    CharismaticSong = 1
    ShadowClaw = 2
    GnawingDread = 9
    
    FuzzyCheeks = 20
    
class cardType(Enum):
    Action = 0
    Magic = 1
    Item = 2
    Hero = 3
    Leader = 4
    Monster = 5
    Any = 6

class heroType(Enum):
    NoClass = 0
    Thief = 1
    Guardian = 2
    Ranger = 3
    Fighter = 4
    Bard = 5
    Wizard = 6
    Berserker = 7
    Necromancer = 8
    Warrior = 9
    Druid = 10
    Sorcerer = 11

class originalGame(Enum):
    Base = 0
    WaD = 1
    BaN = 2
    BQ = 3
    DS = 4
    ME = 5
    HereToSleigh = 6

#Cards
#Party Leaders
Leaders = {
    "Charismatic Song" : {
        "Class" : heroType.Bard,
        "Effect" : cardEffect.CharismaticSong,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Type" : cardType.Leader,
        "Description" : "Each time you roll to use a Hero card's effect, +1 to your roll."
    },
    "Shadow Claw" : {
        "Class" : heroType.Thief,
        "Effect" : cardEffect.ShadowClaw,
        "Activatable" : True,
        "DLC" : originalGame.Base,
        "Type" : cardType.Leader,
        "Description" : "Once per turn on your turn, you may spend an action point to pull a card from another player's hand."
    },
    "Gnawing Dread" : {
        "Class" : heroType.Necromancer,
        "Effect" : cardEffect.GnawingDread,
        "Activatable" : True,
        "DLC" : originalGame.BaN,
        "Type" : cardType.Leader,
        "Description" : "Once per turn on your turn, you may spend 2 action points to search the discard pile for a card and add it to your hand."
    }
    
}
#Monsters
Monsters = {}
#Action
Action = {}
#Magic
Magic = {}
#Items
Items = {}
#Heroes
Heroes = {}
