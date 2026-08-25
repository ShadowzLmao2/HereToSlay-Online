from enum import Enum
testingPhase = True

WarriorsAndDruids  = True
BerserkersAndNecromancers = False
DragonSorcerers = False
BannerQuest = False
HereToSleigh = False
MonsterExpansion = False
KSEandLimited = False
maxHeroes = 5 + WarriorsAndDruids + BerserkersAndNecromancers
ExtraEnemyMonsterSlot = False
if MonsterExpansion == False:
    ExtraEnemyMonsterSlot = False
#Ranked
ranked = False
maxRankedCards = 60
minRankedCards = 40
class languages(Enum):
    English = 0 #Full Support
    Italian = 1 #Base Game and WaD
    German  = 2 #Base Game
    French  = 3 #Todo
    Spanish = 4 #Hire Someone
    Japanese = 5 #To finish learning
    Korean = 6 #Hire someone
language = 0    