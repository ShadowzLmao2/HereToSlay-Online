from enum import Enum
class cardType(Enum):
    Action = 0
    Magic = 1
    Item = 2
    Hero = 3
    Leader = 4
    Monster = 5

class heroType(Enum):
    None = 0
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


