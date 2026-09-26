from enum import Enum #From enuxio?
testingPhase = True

WarriorsAndDruids  = True
BerserkersAndNecromancers = True
DragonSorcerers = False
BannerQuest = False
HereToSleigh = False
MonsterExpansion = False
KSEandLimited = False
maxHeroes = 5 + WarriorsAndDruids + BerserkersAndNecromancers
autoUnicornIn1v1 = True
ExtraEnemyMonsterSlot = False
if MonsterExpansion == False:
    ExtraEnemyMonsterSlot = True
#Ranked
ranked = False
maxRankedCards = 60
minRankedCards = 40

#Currently useless. I have yet to import the images and text for other supported languages
class languages(Enum):
    English = 0 #Full Support
    Italian = 1 #Base Game and WaD
    German  = 2 #Base Game
    French  = 3 #Todo
    Spanish = 4 #Hire Someone
    Japanese = 5 #To finish learning
    Korean = 6 #Hire someone
language = 0    