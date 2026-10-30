from enum import Enum #From enuxio?
testingPhase = True

gamemode = 1 #1 is 1v1 or FFA, 2 is 2v2
WarriorsAndDruids  = False
BerserkersAndNecromancers = False
DragonSorcerers = False
BannerQuest = False
HereToSleigh = False
MonsterExpansion = False
KSEandLimited = False
maxHeroes = 5 + WarriorsAndDruids + BerserkersAndNecromancers
autoUnicornIn1v1 = True
ExtraEnemyMonsterSlot = True
if MonsterExpansion == False:
    ExtraEnemyMonsterSlot = True
askAllToModifyOrChallenge = True
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