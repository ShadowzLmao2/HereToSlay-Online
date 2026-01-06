from enum import Enum
from config import *
class heroEffect(Enum):
    NoEffect        = 0
    #Heroes
    CharismaticSong   = 1
    ShadowClaw        = 2
    DivineArrow       = 3
    CloakedSage       = 4
    ProtectingHorn    = 5
    FistOfReason      = 6
    NobleShaman       = 7
    PiercingHowl      = 8
    GnawingDread      = 9
    RagingManticore   = 10
    FearlessFlame     = 11
    IllusiveTrickster = 12
    VeiledRaider      = 13
    BrutalBow         = 14
    MysticalMaestro   = 15
    UnstableUnicorn   = 16

class cardEffect(Enum):
    NoEffect = 0
    #Action
    Challenge = 1
    Modifier = 2
    #Item
        #Base Game
    BardMask              = 3
    DecoyDoll             = 4
    Mask                  = 5
    ParticularlyRustyCoin = 6
    ReallyBigRing         = 7
        #Warriors and Druids
    BottomlessBag         = 8
    EvenBiggerRing        = 9
    TemporalHourglass     = 10
        #Berserkers and Necromancers
    BiggestRingEver       = 11
    GobletOfCaffeination  = 12
    SilverLining          = 13
        #Dragon Sorcerers
        #KSE
    MysteriousFeather     = 14
    #Cursed Items
    CurseOfTheSnakesEyes  = 15
    SealingKey            = 16
    SuspiciouslyShinyCoin = 17
        #Warriors and Druids
    CursedGlove           = 18
    SoulTether            = 19
        #Berserkers and Necromancers
    DragonsBile           = 20
    SoulboundGrimoire     = 21
        #Dragon Sorcerers
        #KSE
    MaskOfMisfortune      = 22
    
    #Magic
        #Base Game
    CallToTheFallen       = 23
    CriticalBoost         = 24
    DestructiveSpell      = 25
    EnchantedSpell        = 26
    EntanglingTrap        = 27
    ForcedExchange        = 28
    ForcefulWings         = 29
    WindsOfChange         = 30
        #Warriors and Druids
    BeastCall             = 31
    RapidRefresh          = 32
        #Berserkers and Necromancers
    LightningLabrys       = 33
    MassSacrifice         = 34
        #Dragon Sorcerers
    EggOfFortune          = 35
        #KSE
    CapitvatingSpell      = 36   
    #Other Action Cards
    ClassChallenge        = 37
    Draw2Modifier         = 38
    Draw1Modifier         = 39
    DrawIfHigherThanMod   = 40
    SearchDiscIfLowerMod  = 41
    BonusIfAttackingMod   = 42
    DiscardHandModifier   = 43
    Discard1Modifier      = 44
    RuleCard              = 45
    #Heroes
    BadAxe = 46
    BearClaw = 47
    BearyWise = 48
    FuryKnuckle = 49
    HeavyBear = 50
    PanChucks = 51
    QiBear = 52
    ToughTeddy = 53
    DodyDealer = 54
    FuzzyCheeks = 55
    GreedyCheeks = 56
    LuckyBucky = 57
    MellowDee = 58
    NappingNibbles = 59 
    Peanut = 60
    TipsyTootie = 61
    CalmingVoice = 62
    GuidingLight = 63
    HolyCurselifter = 64
    IronResolve = 65
    MightyBlade = 66
    RadiantHorn = 67
    VibrantGlow = 68
    WiseShield = 69
    Bullseye = 70
    Hook = 71
    LookieRookie = 72
    QuickDraw = 73
    SeriousGrey = 74
    SharpFox = 75
    Wildshot = 76
    WilyRed = 77
    KitNapper = 78
    Meowzio = 79
    PlunderingPuma = 80
    Shurikitty = 81
    SilentShadow = 82
    SlipperyPaws = 83
    SliyPickings = 84
    SmoothMimimeow = 85
    BunBun = 86
    Buttons = 87
    Fluffy = 88
    Hopper = 89
    Snowball = 90
    Spooky = 91
    Whiskers = 92
    Wiggles = 93
    #Warriors and Druids
    BigBuckley = 94
    BuckOmens = 95
    DoeFallow = 96
    GlowingAntler = 97
    Majestelk = 98
    MagusMoose = 99
    Maegisty = 100
    Stagguard = 101
    AgileDagger = 102
    BlindingBlade = 103
    CriticalFang = 104
    HardenedHunter = 105
    LootingLupo = 106
    SilentShield = 107
    TenaciousTimber = 108
    WolfgangPack = 109
    #Berserkers and Necromancers
    Annihilator = 110
    BrawlingSpirit = 111
    GruesomeGladioator = 112
    Meowntain = 113
    RabidBeast = 114
    RoaryalGuard = 115
    ViciousWildcat = 116
    UnbridledFury = 117
    BarkHexer = 118
    BeholdenRetriever = 119
    BoneCOllector = 120
    BostonTerror = 121
    GrimPupper = 122
    HollowHusk = 123
    PerfecVessel = 124
    ShadowSaint = 125
    #Dragon Sorcerers
    Distortivern = 126
    Extraga = 127
    Dragalter = 128
    Luut = 129
    Ronvern = 130
    Mirroryu = 131
    Smok = 132
    Oracon = 133
    Shamanaga = 134
    #KSE
    Berserker = 135
    Hamlet = 136
    ComplexIllusion = 137
    Enchantlter = 138
    Hoodwink = 139
    PurringBandit = 140
    NimbleGray = 141
    Mimi = 142
    
    
class monsterEffect(Enum):
    noEffect          = 0
    abyssQueen        = 1
    anuranCauldron    = 2
    arcticAries       = 3
    bloodwing         = 4
    corruptedSabretooth = 5
    crownedSerpent    = 6
    darkDragonKing    = 7
    dracos            = 8
    malamammoth       = 9
    megaSlime         = 10
    orthus            = 11
    rexMajor          = 12
    terratuga         = 13
    titanWyvern       = 14
    warwornOwlbear    = 15
    #WaD
    feralDragon       = 16
    muscipulaRex      = 17
    #BaN
    doombringer       = 18
    reptilianRipper   = 19
    #MoEx
    ancientMegashark  = 20
    clawedNightmare   = 21
    dragonWasp        = 22
    goretelodont      = 23
    lumberingDemon    = 24
    possessedPlush    = 25
    reefRipper        = 26
    saffyrePhoenix    = 27
    scavengerGriffin  = 28
    venemousGemini    = 29
    voltclawLion      = 30
    wanderingBehemoth = 31
    wickedSeaSerpent  = 32
    #BanQ
    chitinScourge     = 33
    razorTongue       = 34
    
class cardType(Enum):
    NoCard  = 0
    Action  = 1
    Magic   = 2
    Item    = 3
    Hero    = 4
    Leader  = 5
    Monster = 6
    Any     = 7
    Challenge = 8 #Monster Expansion only

class heroType(Enum):
    NoClass     = 0
    Thief       = 1
    Guardian    = 2
    Ranger      = 3
    Fighter     = 4
    Bard        = 5
    Wizard      = 6
    Berserker   = 7
    Necromancer = 8
    Warrior     = 9
    Druid       = 10
    Sorcerer    = 11

class originalGame(Enum):
    Base = 0
    WaD  = 1
    BaN  = 2
    BanQ = 3
    DrSo = 4
    MoEx = 5
    HtSleigh = 6
    KSE  = 7

class monsterRollEffect(Enum):
    slay         = 0
    discard      = 1
    sacrifice    = 2
    discardHand  = 3 #BaN Expansion
    sacrificeTwo = 4 #BaN Expansion

class MoExAtkReq(Enum):
    noReq = 0
    discard = 1
    discardTwo = 2
    discardSpecific = 3
    heroClass = 4
    
#Cards
#Party Leaders
Leaders = {
    "None" : {
        "Description" : "Temporary placeholder for src/active_player.py"
    },
    "Charismatic Song" : {
        "Class" : heroType.Bard,
        "Effect" : heroEffect.CharismaticSong,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Description" : "Each time you roll to use a Hero card's effect, +1 to your roll."
    },
    "Fist of Reason" : {
        "Class" : heroType.Fighter,
        "Effect" : heroEffect.FistOfReason,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Description" : "Each time you roll to CHALLENGE, +2 to your roll."
    },
    "Shadow Claw" : {
        "Class" : heroType.Thief,
        "Effect" : heroEffect.ShadowClaw,
        "Activatable" : True,
        "DLC" : originalGame.Base,
        "Description" : "Once per turn on your turn, you may spend an action point to pull a card from another player's hand."
    },
    "Cloaked Sage" : {
        "Class" : heroType.Wizard,
        "Effect" : heroEffect.CloakedSage,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Description" : "Each time you play a Magic card, DRAW a card."
    },
    "Divine Arrow" : {
        "Class" : heroType.Ranger,
        "Effect" : heroEffect.DivineArrow,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Description" : "Each time you roll to ATTACK a Monster card, +1 to your roll."
    },
    "Protecting Horn" : {
        "Class" : heroType.Guardian,
        "Effect" : heroEffect.ProtectingHorn,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Description" : "Each time you play a Modifier card on a roll, +1 or -1 to that roll."
    },
    "Noble Shaman" : {
        "Class" : heroType.Druid,
        "Effect" : heroEffect.NobleShaman,
        "Activatable" : False,
        "DLC" : originalGame.WaD,
        "Description" : "Once per turn on each player's turn, you may choose any player's roll. -1 to that roll."
    },
    "Piercing Howl" : {
        "Class" : heroType.Warrior,
        "Effect" : heroEffect.PiercingHowl,
        "Activatable" : False,
        "DLC" : originalGame.WaD,
        "Description" : "Each time you roll, +1 to your roll for each Item card equipped to a Hero card in your party."
    },
    "Gnawing Dread" : {
        "Class" : heroType.Necromancer,
        "Effect" : heroEffect.GnawingDread,
        "Activatable" : True,
        "DLC" : originalGame.BaN,
        "Description" : "Once per turn on your turn, you may spend 2 action points to search the discard pile for a card and add it to your hand."
    },
    "Raging Manticore" : {
        "Class" : heroType.Berserker,
        "Effect" : heroEffect.RagingManticore,
        "Activatable" : False,
        "DLC" : originalGame.BaN,
        "Description" : "Each time you SLAY a Monster card, DRAW 2 cards."
    },
    "Fearless Flame" : {
        "Class" : heroType.Sorcerer,
        "Effect" : heroEffect.FearlessFlame,
        "Activatable" : False,
        "DLC" : originalGame.DrSo,
        "Description" : "Each time you roll the dice, you may DISCARD a card. If you do, +1 to your roll."
    },
    "Brutal Bow" : {
        "Class" : heroType.Fighter,
        "Secondary Class" : heroType.Ranger,
        "Effect" : heroEffect.BrutalBow,
        "Activatable" : False,
        "DLC" : originalGame.KSE,
        "Description" : "At the beginning of your turn, you may switch The Brutal Bow's class between Fighter and Ranger.\nEach time you DESTROY a Hero card, DRAW a card."
    },
    "Mystical Maestro" : {
        "Class" : heroType.Wizard,
        "Secondary Class" : heroType.Bard,
        "Effect" : heroEffect.MysticalMaestro,
        "Activatable" : False,
        "DLC" : originalGame.KSE,
        "Description" : "At the beginning of your turn, you may switch The Mystical Maestro's class between Mage and Bard.\nEach time you roll 4 or less (including Modifier cards), you may DRAW a card."
    },
    "Veiled Raider" : {
        "Class" : heroType.Guardian,
        "Secondary Class" : heroType.Thief,
        "Effect" : heroEffect.VeiledRaider,
        "Activatable" : False,
        "DLC" : originalGame.KSE,
        "Description" : "At the beginning of your turn, you may switch The Veiled Raider's class between Guardian and Thief.\nEach time you roll 12 or more (including Modifier cards), you may STEAL a Hero."
    },
    "Unstable Unicorn" : {
        "Class" : heroType.NoClass,
        "Effect" : heroEffect.UnstableUnicorn,
        "Activatable" : False,
        "DLC" : originalGame.KSE,
        "Description" : "The Unstable Unicorn has no class. At the beginning of your turn, you may choose another player's Party Leader card. The Unstable Unicorn's skill is that Party Leader card's skill until your next turn."
    },
    
}
#Monsters
Monsters = {
    "None" : {
        "Description" : "Temporary placeholder for src/active_player.py"
    },
    "Abyss Queen" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 5,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.abyssQueen,
        "Description" : "Each time another player plays a Modifier card on one of your rolls, +1 to your roll."
    },
    "Anuran Cauldron" : {
        "Hero Req"    : 3,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.anuranCauldron,
        "Description" : "Each time you roll, +1 to your roll."
    },
    "Arctic Aries" : {
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 10,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.arcticAries,
        "Description" : "Each time you successfully roll to use a Hero card's effect, you may DRAW a card."
    },
    "Bloodwing" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.bloodwing,
        "Description" : "Each time another player CHALLENGES you, that player must DISCARD a card."
    },
    "Corrupted Sabreetooth" : {
        "Hero Req"    : 3,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.corruptedSabretooth,
        "Description" : "Each time you would DESTROY a Hero card, you may STEAL that Hero card instead."
    },
    "Crowned Serpent" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 7,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 10,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.crownedSerpent,
        "Description" : "Each time any player (including you) plays a Modifier card, you may DRAW a card."
    },
    "Dark Dragon King" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.Bard,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.darkDragonKing,
        "Description" : "Each time you roll for a Hero card's effect, +1 to your roll."
    },
    "Dracos" : {
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 5,
        "Lose Effect" : monsterRollEffect.slay,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.sacrifice,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.dracos,
        "Description" : "Each time a Hero card in your Party is destroyed, you may DRAW a card."
    },
    "Malamammoth" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.Ranger,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.malamammoth,
        "Description" : "Each time you DRAW an Item card, you may play it immediately."
    },
    "Mega Slime" : {
        "Hero Req"    : 4,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 7,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.megaSlime,
        "Description" : "You may spend an extra action point on each of your turns."
    },
    "Orthus" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.Wizard,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.orthus,
        "Description" : "Each time you DRAW a Magic card, you may play it immediately."
    },
    "Rex Major" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.Guardian,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.rexMajor,
        "Description" : "Each time you DRAW a Modifier card, you may reveal it and DRAW a second card."
    },
    "Terratuga" : {
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 7,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 11,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.terratuga,
        "Description" : "Your Hero cards cannot be destroyed."
    },
    "Titan Wyvern" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.Fighter,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.titanWyvern,
        "Description" : "Each time you roll for a Challenge card, +1 to your roll."
    },
    "Warworn Owlbear" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.Thief,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.Base,
        "Effect"      : monsterEffect.warwornOwlbear,
        "Description" : "Item cards you play cannot be challenged."
    },
    #Warriors and Druids Monsters
    "Feral Dragon" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.WaD,
        "Effect"      : monsterEffect.feralDragon,
        "Description" : "Each time any player sacrifices a card, DRAW a card."
    },
    "Muscipula Rex" : {
        "Hero Req"    : 3,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 7,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 10,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.WaD,
        "Effect"      : monsterEffect.feralDragon,
        "Description" : "Once per turn on your turn, you may DRAW a card without spending an action point."
    },
    #Berserkers and Necromancers Monsters
    "Doombringer" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.Necromancer,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discardHand,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.BaN,
        "Effect"      : monsterEffect.doombringer,
        "Description" : "Each time you SACRIFICE a card, you mamy choose a card from the discard pile, add it to your hand."
    },
    "Reptilian Ripper" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.Berserker,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrificeTwo,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.BaN,
        "Effect"      : monsterEffect.reptilianRipper,
        "Description" : "Each time you roll to ATTACK a Monster card, +2 to your roll."
    },
    "Ancient Megashark" : {
        "Hero Req"    : 1,
        "MoEx AtkReq" : MoExAtkReq.discard,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.ancientMegashark,
        "Description" : "Each time you roll to ATTACK a Monster card, +1 to that roll."
    },
    "Clawed Nightmare" : {
        "Hero Req"    : 3,
        "MoEx AtkReq" : MoExAtkReq.heroClass,
        "Class Req"   : heroType.Bard,
        "Class Req 2" : heroType.Thief,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.clawedNightmare,
        "Description" : "Each time you end your turn with no cards in your hands, you may pull 2 cards from another player's hand."
    },
    "Dragon Wasp" : {
        "Hero Req"    : 1,
        "MoEx AtkReq" : MoExAtkReq.discardTwo,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.dragonWasp,
        "Description" : "Each time one of your Hero cards would be sacrificed or destroyed, you may DISACRD 2 cards instead."
    },
    "Goretelodont" : {
        "Hero Req"    : 3,
        "MoEx AtkReq" : MoExAtkReq.heroClass,
        "Class Req"   : heroType.Guardian,
        "Class Req 2" : heroType.Ranger,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.goretelodont,
        "Description" : "Each time you end your turn with no cards in your hand, you may DRAW 3 cards."
    },
    "Lumbering Demon" : {
        "Hero Req"    : 2,
        "MoEx AtkReq" : MoExAtkReq.noReq,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 5,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.lumberingDemon,
        "Description" : "Each time you would DRAW a card, you may DRAW 2 cards and DISCARD a card instead."
    },
    "Possessed Plush" : {
        "Hero Req"    : 1,
        "MoEx AtkReq" : MoExAtkReq.discardSpecific,
        "Spec Discard": cardType.Challenge,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.possessedPlush,
        "Description" : "Each time you play a Challenge card, DRAW a card."
    },
    "Reef Ripper" : {
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.slay,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.sacrifice,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.reefRipper,
        "Description" : "Each time you unsuccessfully roll to use a Hero card's effect, you may DRAW a card."
    },
    "Saffyre Phoenix" : {
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 8,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 13,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.saffyrePhoenix, #remember to add the +2 per Hero bonus
        "Description" : "Each time one of your Hero cards is sacrificed or destroyed, you may play a Hero card from your hand immediately."
    },
    "Scavenger Griffin" : {
        "Hero Req"    : 3,
        "MoEx AtkReq" : MoExAtkReq.heroClass,
        "Class Req"   : heroType.Fighter,
        "Class Req 2" : heroType.Wizard,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.scavengerGriffin,
        "Description" : "Each time you end your turn with no cards in your hand, you may STEAL a Hero card."
    },
    "Venomous Gemini" : {
        "Hero Req"    : 5,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.venemousGemini,
        "Description" : "Venomous Gemini counts for 2 Monsters."
    },
    "Voltclaw Lion" : {
        "Hero Req"    : 1,
        "MoEx AtkReq" : MoExAtkReq.discardSpecific,
        "Spec Discard": cardType.Magic,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.voltclawLion,
        "Description" : "Each time you play a Magic card, DRAW a card."
    },
    "Wandering Behemoth" : {
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 10,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.wanderingBehemoth, #remember to add the +1 per Hero bonus
        "Description" : "Each time one of your Hero cards is sacrificed or destroyed, you may DRAW a card."
    },
    "Wicked Sea Serpent" : {
        "Hero Req"    : 1,
        "MoEx AtkReq" : MoExAtkReq.discardSpecific,
        "Spec Discard": cardType.Item,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.MoEx,
        "Effect"      : monsterEffect.wickedSeaSerpent,
        "Description" : "Each time you play an Item card, DRAW a card."
    },
    "Chitin Scourge" : {
        "Hero Req"    : 3,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.BanQ,
        "Effect"      : monsterEffect.chitinScourge,
        "Description" : "Each time another player rolls to ATTACK a Monster card, -1 to that roll."
    },
    "Razor Tongue" : {
        "Hero Req"    : 2,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 5,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "DLC"         : originalGame.BanQ,
        "Effect"      : monsterEffect.razorTongue,
        "Description" : "Each time another player discards any number of cards, DRAW a card."
    },
}
#Action
Action = {
    "None" : {
        "Description" : "Temporary placeholder for src/active_player.py"
    }
}
#Magic
Magic = {
    "None" : {
        "Description" : "Temporary placeholder for src/active_player.py"
    }
}
#Items
Items = {
    "None" : {
        "Description" : "Temporary placeholder for src/active_player.py"
    }
}
#Heroes
Heroes = {
    "None" : {
        "Description" : "Temporary placeholder for src/active_player.py"
    }
}
#Banners
Banners = {
    "None" : {
        "Description" : "Temporary placeholder for src/active_player.py"
    }
}

#Main Deck
mainDeck = [1,2,3,4,5]
monsterDeck = [
    "Abyss Queen",
    "Anuran Cauldron",
    "Arctic Aries",
    "Bloodwing",
    "Corrupted Sabretooth",
    "Crowned Serpent",
    "Dark Dragon King",
    "Dracos",
    "Malamammoth",
    "Mega Slime",
    "Orthus",
    "Rex Major",
    "Terratuga",
    "Titan Wyvern",
    "Warworn Owlbear"
    ]
wadDeck = ["Feral Dragon","Muscipula Rex"]
banDeck = ["Doom Bringer","Reptilian Ripper"]
moeDeck = [
    "Ancient Megashark",
    "Clawed Nightmare",
    "Dragon Wasp",
    "Goreteledont",
    "Lumbeering Demon",
    "Possessed Plush",
    "Reef Ripper",
    "Saffyre Phoenix",
    "Scavenger Griffin",
    "Venemous Gemini",
    "Voltclaw Lion",
    "Wandering Behemoth",
    "Wicked Sea Serpent",
    ]
baqDeck = ["Chiting Scourge","Razor Tongue"]
if WarriorsAndDruids:
    monsterDeck.append(wadDeck)
if BerserkersAndNecromancers:
    monsterDeck.append(banDeck)
if MonsterExpansion:
    monsterDeck.append(moeDeck)
if BannerQuest:
    monsterDeck.append(baqDeck)
    
rankedMainDeck = []
rankedMonsterDeck = [
    "Abyss Queen",
    "Anuran Cauldron",
    "Arctic Aries",
    "Bloodwing",
    "Corrupted Sabretooth",
    "Crowned Serpent",
    "Dark Dragon King",
    "Dracos",
    "Malamammoth",
    "Mega Slime",
    "Orthus",
    "Rex Major",
    "Terratuga",
    "Titan Wyvern",
    "Warworn Owlbear",
    "Feral Dragon",
    "Muscipula Rex",
    "Doom Bringer",
    "Reptilian Ripper",
    "Ancient Megashark",
    "Clawed Nightmare",
    "Dragon Wasp",
    "Goreteledont",
    "Lumbeering Demon",
    "Possessed Plush",
    "Reef Ripper",
    "Saffyre Phoenix",
    "Scavenger Griffin",
    "Venemous Gemini",
    "Voltclaw Lion",
    "Wandering Behemoth",
    "Wicked Sea Serpent",
    "Chiting Scourge",
    "Razor Tongue"
    ]
