from enum import Enum
from config import *
from draw import *
from data import *
class heroEffect(Enum):
    NoEffect          = 0
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
    VeiledRaider      = 12
    BrutalBow         = 13
    MysticalMaestro   = 14
    FiercePanguardian = 15
    IllusiveTrickster = 16
    RhythmicArcher    = 17
    UnstableUnicorn   = 18

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
    ForcefulWinds         = 29
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
    DrawIfAboveModifier   = 40
    SearchDiscBelowMod    = 41
    AtkBonusModifier      = 42
    DiscardHandModifier   = 43
    Discard1Modifier      = 44
    RuleCard              = 45
    #Heroes
    BadAxe          = 46
    BearyWise       = 47
    HeavyBear       = 48
    PanChucks       = 49
    QiBear          = 50
    ToughTeddy      = 51
    DodgyDealer     = 52
    FuzzyCheeks     = 53
    GreedyCheeks    = 54
    LuckyBucky      = 55
    MellowDee       = 56
    TipsyTootie     = 57
    CalmingVoice    = 58
    HolyCurselifter = 59
    IronResolve     = 60
    MightyBlade     = 61
    VibrantGlow     = 62
    WiseShield      = 63
    Bullseye        = 64
    Hook            = 66
    QuickDraw       = 67
    SeriousGrey     = 67
    SharpFox        = 68
    Wildshot        = 69
    WilyRed         = 70
    Meowzio         = 71
    PlunderingPuma  = 72
    Shurikitty      = 73
    SilentShadow    = 74
    SlipperyPaws    = 75
    SmoothMimimeow  = 76
    BunBun          = 77
    Fluffy          = 78
    Hopper          = 79
    Snowball        = 80
    Spooky          = 81
    Whiskers        = 82
    Wiggles         = 83
    #Warriors and Druids
    BigBuckley      = 84
    BuckOmens       = 85
    DoeFallow       = 86
    Majestelk       = 87
    MagusMoose      = 88
    Maegisty        = 89
    Stagguard       = 90
    BlindingBlade   = 91
    CriticalFang    = 92
    HardenedHunter  = 93
    LootingLupo     = 94
    SilentShield    = 95
    TenaciousTimber = 96
    WolfgangPack    = 97
    #Berserkers and Necromancers
    Annihilator        = 98
    BrawlingSpirit     = 99
    GruesomeGladiator  = 100
    Meowntain          = 101
    RabidBeast         = 102
    RoaryalGuard       = 103
    ViciousWildcat     = 104
    UnbridledFury      = 105
    BarkHexer          = 106
    BeholdenRetriever  = 107
    BoneCollector      = 108
    BostonTerror       = 109
    GrimPupper         = 110
    HollowHusk         = 111
    PerfectVessel      = 112
    ShadowSaint        = 113
    #Dragon Sorcerers
    Dystortivern       = 114
    Extraga            = 115
    Dragalter          = 116
    Luut               = 117
    Renovern           = 118
    Mirroryu           = 119
    Smok               = 120
    Oracon             = 121
    Shamanaga          = 122
    #KSE
    Bearserker         = 123
    Hamlet             = 124
    ComplexIllusion    = 125
    Enchantler         = 126
    Hoodwink           = 127
    PurringBandit      = 128
    NimbleGray         = 129
    Mimi               = 130

    PullCard           = 131
    ForceDiscard       = 132
    Draw2              = 133
    SearchDiscard      = 134
    StealHero          = 135
    PullAndPlay        = 136
    Play2              = 137
    
    OneModifier = 138
    
    
    
class monsterEffect(Enum):
    noEffect            = 0
    abyssQueen          = 1
    anuranCauldron      = 2
    arcticAries         = 3
    bloodwing           = 4
    corruptedSabretooth = 5
    crownedSerpent      = 6
    darkDragonKing      = 7
    dracos              = 8
    malamammoth         = 9
    megaSlime           = 10
    orthus              = 11
    rexMajor            = 12
    terratuga           = 13
    titanWyvern         = 14
    warwornOwlbear      = 15
    #WaD
    feralDragon         = 16
    muscipulaRex        = 17
    #BaN
    doombringer         = 18
    reptilianRipper     = 19
    #MoEx
    ancientMegashark    = 20
    clawedNightmare     = 21
    dragonWasp          = 22
    goretelodont        = 23
    lumberingDemon      = 24
    possessedPlush      = 25
    reefRipper          = 26
    saffyrePhoenix      = 27
    scavengerGriffin    = 28
    venemousGemini      = 29
    voltclawLion        = 30
    wanderingBehemoth   = 31
    wickedSeaSerpent    = 32
    #BanQ
    chitinScourge       = 33
    razorTongue         = 34
    
class cardType(Enum):
    NoCard    = 0
    Action    = 1
    Magic     = 2
    Item      = 3
    Hero      = 4
    Leader    = 5
    Monster   = 6
    Any       = 7
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

class monsterRollEffect(Enum):
    slay         = 0
    discard      = 1
    sacrifice    = 2
    discardHand  = 3 #BaN Expansion
    sacrificeTwo = 4 #BaN Expansion
    discardTwo   = 5 #DSE

class MoExAtkReq(Enum):
    noReq           = 0
    discard         = 1
    discardTwo      = 2
    discardSpecific = 3
    heroClass       = 4
    
#Cards
#Party Leaders

Leaders = {
    "None" : {
        "Description" : "None",
        "Start of Turn" : False,
        }, #TODO Backslashes
    "Charismatic Song" : {
        "Image" : 'src\data\card_images\BaseGame\Leaders\charismaticSong.png',
        "Class" : heroType.Bard,
        "Effect" : heroEffect.CharismaticSong,
        "Activatable" : False,
        #"Image" : originalGame.BaseGame,
        "Description" : "Each time you roll to use a Hero card's effect, +1 to your roll."
    },
    "Fist of Reason" : {
        "Image" : 'src\data\card_images\BaseGame\Leaders\fistOfReason.png',
        "Class" : heroType.Fighter,
        "Effect" : heroEffect.FistOfReason,
        "Activatable" : False,
        "Description" : "Each time you roll to CHALLENGE, +2 to your roll."
    },
    "Shadow Claw" : {
        "Image" : 'src\data\card_images\BaseGame\Leaders\shadowClaw.png',
        "Class" : heroType.Thief,
        "Effect" : heroEffect.ShadowClaw,
        "Activatable" : True,
        "Description" : "Once per turn on your turn, you may spend an action point to pull a card from another player's hand."
    },
    "Cloaked Sage" : {
        "Image" : 'src\data\card_images\BaseGame\Leaders\cloakedSage.png',
        "Class" : heroType.Wizard,
        "Effect" : heroEffect.CloakedSage,
        "Activatable" : False,
        "Description" : "Each time you play a Magic card, DRAW a card."
    },
    "Divine Arrow" : {
        "Image" : 'src\data\card_images\BaseGame\Leaders\divineArrow.png',
        "Class" : heroType.Ranger,
        "Effect" : heroEffect.DivineArrow,
        "Activatable" : False,
        "Description" : "Each time you roll to ATTACK a Monster card, +1 to your roll."
    },
    "Protecting Horn" : {
        "Image" : 'src\data\card_images\BaseGame\Leaders\protectingHorn.png',
        "Class" : heroType.Guardian,
        "Effect" : heroEffect.ProtectingHorn,
        "Activatable" : False,
        "Description" : "Each time you play a Modifier card on a roll, +1 or -1 to that roll."
    },
    "Noble Shaman" : {
        "Image" : 'src\data\card_images\WarriorsAndDruids\Leaders\nobleShaman.png',
        "Class" : heroType.Druid,
        "Effect" : heroEffect.NobleShaman,
        "Activatable" : False,
        "Description" : "Once per turn on each player's turn, you may choose any player's roll. -1 to that roll."
    },
    "Piercing Howl" : {
        "Image" : 'src\data\card_images\WarriorsAndDruids\Leaders\piercingHowl.png',
        "Class" : heroType.Warrior,
        "Effect" : heroEffect.PiercingHowl,
        "Activatable" : False,
        "Description" : "Each time you roll, +1 to your roll for each Item card equipped to a Hero card in your party."
    },
    "Gnawing Dread" : {
        "Image" : 'src\data\card_images\BerserkersAndNecromancers\Leaders\gnawingDread.png',
        "Class" : heroType.Necromancer,
        "Effect" : heroEffect.GnawingDread,
        "Activatable" : True,

        "Description" : "Once per turn on your turn, you may spend 2 action points to search the discard pile for a card and add it to your hand."
    },
    "Raging Manticore" : {
        "Image" : 'src\data\card_images\BerserkersAndNecromancers\Leaders\ragingManticore.png',
        "Class" : heroType.Berserker,
        "Effect" : heroEffect.RagingManticore,
        "Activatable" : False,
        "Description" : "Each time you SLAY a Monster card, DRAW 2 cards."
    },
    "Fearless Flame" : {
        "Image" : 'src\data\card_images\DragonSorcerers\Leaders\fearlessFlame.png',
        "Class" : heroType.Sorcerer,
        "Effect" : heroEffect.FearlessFlame,
        "Activatable" : False,
        "Description" : "Each time you roll the dice, you may DISCARD a card. If you do, +1 to your roll."
    },
    "Brutal Bow" : {
        "Image" : 'src\data\card_images\KSE\Leaders\brutalBow.png',
        "Class" : heroType.Fighter,
        "Secondary Class" : heroType.Ranger,
        "Effect" : heroEffect.BrutalBow,
        "Activatable" : False,
        "Start of Turn" : True,
        "Description" : "At the beginning of your turn, you may switch The Brutal Bow's class between Fighter and Ranger.\nEach time you DESTROY a Hero card, DRAW a card."
    },
    "Mystical Maestro" : {
        "Image" : 'src\data\card_images\KSE\Leaders\mysticalMaestro.png',
        "Class" : heroType.Wizard,
        "Secondary Class" : heroType.Bard,
        "Effect" : heroEffect.MysticalMaestro,
        "Activatable" : False,
        "Start of Turn" : True,
        "Description" : "At the beginning of your turn, you may switch The Mystical Maestro's class between Mage and Bard.\nEach time you roll 4 or less (including Modifier cards), you may DRAW a card."
    },
    "Veiled Raider" : {
        "Image" : 'src\data\card_images\KSE\Leaders\veiledRaider.png',
        "Class" : heroType.Guardian,
        "Secondary Class" : heroType.Thief,
        "Effect" : heroEffect.VeiledRaider,
        "Activatable" : False,
        "Start of Turn" : True,
        "Description" : "At the beginning of your turn, you may switch The Veiled Raider's class between Guardian and Thief.\nEach time you roll 12 or more (including Modifier cards), you may STEAL a Hero."
    },
    "Unstable Unicorn" : {
        "Image" : 'src\data\card_images\KSE\Leaders\unstableUnicorn.png',
        "Class" : heroType.NoClass,
        "Effect" : heroEffect.UnstableUnicorn,
        "Activatable" : False,
        "Start of Turn" : True,
        "Description" : "The Unstable Unicorn has no class. At the beginning of your turn, you may choose another player's Party Leader card. The Unstable Unicorn's skill is that Party Leader card's skill until your next turn."
    },
    "Fierce Panguardian" : {
        "Image" : 'src\data\card_images\KSE\IndividualExclusives\fiercePanguardian.png',
        "Class" : heroType.Fighter,
        "Secondary Class" : heroType.Guardian,
        "Effect" : heroEffect.FiercePanguardian,
        "Activatable" : False,
        "Start of Turn" : True,
        "Description" : "At the beginning of your turn, you may switch The Fierce Panguardian's class between Guardian and Fighter.\nEach time you CHALLENGE another player's card, that player cannot play Modifier cards until the end of the turn."
    },
    "Illusive Trickster" : {
        "Image" : 'src\data\card_images\KSE\IndividualExclusives\illusiveTrickster.png',
        "Class" : heroType.Thief,
        "Secondary Class" : heroType.Wizard,
        "Effect" : heroEffect.IllusiveTrickster,
        "Activatable" : True,
        "Start of Turn" : True,
        "Description" : "At the beginning of your turn, you may switch The Illusive Trickster's class between Wizard and Thief.\nOnce per turn on your turn, you may DISCARD a Magic card, then DRAW 3 cards."
    },
    "Rhythmic Archer" : {
        "Image" : 'src\data\card_images\KSE\IndividualExclusives\rhythmicArcher.png',
        "Class" : heroType.Ranger,
        "Secondary Class" : heroType.Bard,
        "Effect" : heroEffect.RhythmicArcher,
        "Activatable" : False,
        "Start of Turn" : True,
        "Description" : "At the beginning of your turn, you may switch The Rhythmic Archers's class between Bard and Ranger.\nEach time any player (including you) unsuccessfully rolls ot ATTACK a Monster card, you may DRAW a card."
    },
}
#Monsters
Monsters = {
    "Abyss Queen" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\abyssQueen.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 5,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.abyssQueen,
        "Description" : "Each time another player plays a Modifier card on one of your rolls, +1 to your roll."
    },
    "Anuran Cauldron" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\anuranCauldron.png',
        "Hero Req"    : 3,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.anuranCauldron,
        "Description" : "Each time you roll, +1 to your roll."
    },
    "Arctic Aries" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\arcticAries.png',
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 10,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.arcticAries,
        "Description" : "Each time you successfully roll to use a Hero card's effect, you may DRAW a card."
    },
    "Bloodwing" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\bloodwing.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.bloodwing,
        "Description" : "Each time another player CHALLENGES you, that player must DISCARD a card."
    },
    "Corrupted Sabreetooth" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\corruptedSabretooth.png',
        "Hero Req"    : 3,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.corruptedSabretooth,
        "Description" : "Each time you would DESTROY a Hero card, you may STEAL that Hero card instead."
    },
    "Crowned Serpent" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\crownedSerpent.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 7,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 10,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.crownedSerpent,
        "Description" : "Each time any player (including you) plays a Modifier card, you may DRAW a card."
    },
    "Dark Dragon King" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\darkDragonKing.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.Bard,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.darkDragonKing,
        "Description" : "Each time you roll for a Hero card's effect, +1 to your roll."
    },
    "Dracos" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\dracos.png',
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 5,
        "Lose Effect" : monsterRollEffect.slay,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.sacrifice,
        "Effect"      : monsterEffect.dracos,
        "Description" : "Each time a Hero card in your Party is destroyed, you may DRAW a card."
    },
    "Malamammoth" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\malamammoth.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.Ranger,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.malamammoth,
        "Description" : "Each time you DRAW an Item card, you may play it immediately."
    },
    "Mega Slime" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\megaSlime.png',
        "Hero Req"    : 4,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 7,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.megaSlime,
        "Description" : "You may spend an extra action point on each of your turns."
    },
    "Orthus" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\orthus.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.Wizard,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.orthus,
        "Description" : "Each time you DRAW a Magic card, you may play it immediately."
    },
    "Rex Major" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\rexMajor.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.Guardian,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.rexMajor,
        "Description" : "Each time you DRAW a Modifier card, you may reveal it and DRAW a second card."
    },
    "Terratuga" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\terratuga.png',
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 7,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 11,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.terratuga,
        "Description" : "Your Hero cards cannot be destroyed."
    },
    "Titan Wyvern" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\titanWyvern.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.Fighter,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.titanWyvern,
        "Description" : "Each time you roll for a Challenge card, +1 to your roll."
    },
    "Warworn Owlbear" : {
        "Image" : 'src\data\card_images\BaseGame\Monsters\warwornOwlbear.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.Thief,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.warwornOwlbear,
        "Description" : "Item cards you play cannot be challenged."
    },
    #Warriors and Druids Monsters
    "Feral Dragon" : {
        "Image" : 'src\data\card_images\WarriorsAndDruids\Monsters\feralDragon.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.feralDragon,
        "Description" : "Each time any player sacrifices a card, DRAW a card."
    },
    "Muscipula Rex" : {
        "Image" : 'src\data\card_images\WarriorsAndDruids\Monsters\muscipulaRex.png',
        "Hero Req"    : 3,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 7,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 10,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.feralDragon,
        "Description" : "Once per turn on your turn, you may DRAW a card without spending an action point."
    },
    #Berserkers and Necromancers Monsters
    "Doombringer" : {
        "Image" : 'src/data/card_images/BerserkersAndNecromancers/Monsters/doombringer.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.Necromancer,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discardHand,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.doombringer,
        "Description" : "Each time you SACRIFICE a card, you may choose a card from the discard pile, add it to your hand."
    },
    "Reptilian Ripper" : {
        "Image" : 'src/data/card_images/BerserkersAndNecromancers/Monsters/reptilianRipper.png',
        "Hero Req"    : 2,
        "Class Req"   : heroType.Berserker,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrificeTwo,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.reptilianRipper,
        "Description" : "Each time you roll to ATTACK a Monster card, +2 to your roll."
    },
    "Ancient Megashark" : {
        "Image" : 'src/data/card_images/MonsterExpansion/ancientMegashark.png',
        "Hero Req"    : 1,
        "MoEx AtkReq" : MoExAtkReq.discard,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.ancientMegashark,
        "Description" : "Each time you roll to ATTACK a Monster card, +1 to that roll."
    },
    "Clawed Nightmare" : {
        "Image" : 'src/data/card_images/MonsterExpansion/clawedNightmare.png',
        "Hero Req"    : 3,
        "MoEx AtkReq" : MoExAtkReq.heroClass,
        "Class Req"   : heroType.Bard,
        "Class Req 2" : heroType.Thief,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.clawedNightmare,
        "Description" : "Each time you end your turn with no cards in your hands, you may pull 2 cards from another player's hand."
    },
    "Dragon Wasp" : {
        "Image" : 'src/data/card_images/MonsterExpansion/dragonWasp.png',
        "Hero Req"    : 1,
        "MoEx AtkReq" : MoExAtkReq.discardTwo,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.dragonWasp,
        "Description" : "Each time one of your Hero cards would be sacrificed or destroyed, you may DISACRD 2 cards instead."
    },
    "Goretelodont" : {
        "Image" : 'src/data/card_images/MonsterExpansion/goretelodont.png',
        "Hero Req"    : 3,
        "MoEx AtkReq" : MoExAtkReq.heroClass,
        "Class Req"   : heroType.Guardian,
        "Class Req 2" : heroType.Ranger,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.goretelodont,
        "Description" : "Each time you end your turn with no cards in your hand, you may DRAW 3 cards."
    },
    "Lumbering Demon" : {
        "Image" : 'src/data/card_images/MonsterExpansion/lumberingDemon.png',
        "Hero Req"    : 2,
        "MoEx AtkReq" : MoExAtkReq.noReq,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 5,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.lumberingDemon,
        "Description" : "Each time you would DRAW a card, you may DRAW 2 cards and DISCARD a card instead."
    },
    "Possessed Plush" : {
        "Image" : 'src/data/card_images/MonsterExpansion/possessedPlush.png',
        "Hero Req"    : 1,
        "MoEx AtkReq" : MoExAtkReq.discardSpecific,
        "Spec Discard": cardType.Challenge,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.possessedPlush,
        "Description" : "Each time you play a Challenge card, DRAW a card."
    },
    "Reef Ripper" : {
        "Image" : 'src/data/card_images/MonsterExpansion/reefRipper.png',
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.slay,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.sacrifice,
        "Effect"      : monsterEffect.reefRipper,
        "Description" : "Each time you unsuccessfully roll to use a Hero card's effect, you may DRAW a card."
    },
    "Saffyre Phoenix" : {
        "Image" : 'src/data/card_images/MonsterExpansion/saffyrePhoenix.png',
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 8,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 13,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.saffyrePhoenix, #remember to add the +2 per Hero bonus
        "Description" : "Each time one of your Hero cards is sacrificed or destroyed, you may play a Hero card from your hand immediately."
    },
    "Scavenger Griffin" : {
        "Image" : 'src/data/card_images/MonsterExpansion/scavengerGriffin.png',
        "Hero Req"    : 3,
        "MoEx AtkReq" : MoExAtkReq.heroClass,
        "Class Req"   : heroType.Fighter,
        "Class Req 2" : heroType.Wizard,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.scavengerGriffin,
        "Description" : "Each time you end your turn with no cards in your hand, you may STEAL a Hero card."
    },
    "Venomous Gemini" : {
        "Image" : 'src/data/card_images/MonsterExpansion/venomousGemini.png',
        "Hero Req"    : 5,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.venemousGemini,
        "Description" : "Venomous Gemini counts for 2 Monsters."
    },
    "Voltclaw Lion" : {
        "Image" : 'src/data/card_images/MonsterExpansion/voltclawLion.png',
        "Hero Req"    : 1,
        "MoEx AtkReq" : MoExAtkReq.discardSpecific,
        "Spec Discard": cardType.Magic,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.voltclawLion,
        "Description" : "Each time you play a Magic card, DRAW a card."
    },
    "Wandering Behemoth" : {
        "Image" : 'src/data/card_images/MonsterExpansion/wanderingBehemoth.png',
        "Hero Req"    : 1,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 10,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.wanderingBehemoth, #remember to add the +1 per Hero bonus
        "Description" : "Each time one of your Hero cards is sacrificed or destroyed, you may DRAW a card."
    },
    "Wicked Sea Serpent" : {
        "Image" : 'src/data/card_images/MonsterExpansion/wickedSeaSerpent.png',
        "Hero Req"    : 1,
        "MoEx AtkReq" : MoExAtkReq.discardSpecific,
        "Spec Discard": cardType.Item,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 7,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.wickedSeaSerpent,
        "Description" : "Each time you play an Item card, DRAW a card."
    },
    #banner quest monsters
    "Chitin Scourge" : {
        "Image" : '',
        "Hero Req"    : 3,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 6,
        "Lose Effect" : monsterRollEffect.sacrifice,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.chitinScourge,
        "Description" : "Each time another player rolls to ATTACK a Monster card, -1 to that roll."
    },
    "Razor Tongue" : {
        "Image" : '',
        "Hero Req"    : 2,
        "Class Req"   : heroType.NoClass,
        "Lose Roll"   : 5,
        "Lose Effect" : monsterRollEffect.discard,
        "Win Roll"    : 9,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.razorTongue,
        "Description" : "Each time another player discards any number of cards, DRAW a card."
    },
    "Calamity Mongrel" : {
        "Image" : '',
        "Hero Req"    : 2,
        "Class Req"   : heroType.Sorcerer,
        "Lose Roll"   : 4,
        "Lose Effect" : monsterRollEffect.discardTwo,
        "Win Roll"    : 8,
        "Win Effect"  : monsterRollEffect.slay,
        "Effect"      : monsterEffect.razorTongue,
        "Description" : "Each time you DRAW a Challenge card, you may DISCARD it and DRAW 2 cards."
    },
    "None" : {
        "Description" : "None"
    }
}
Cards = {
    #Action
    "Challenge" : {
        "Image" : 'src/data/card_images/BaseGame/Cards/challenge.png',
        "Effect" : cardEffect.Challenge,
        "Quantity"    : 14,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card."
    },
    "Fighter Challenge" : {
        "Image" : 'src/data/card_images/KSE/Cards/fighterChallenge.png',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Fighter,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "Bard Challenge" : {
        "Image" : 'src/data/card_images/KSE/Cards/bardChallenge.png',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Bard,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "Guardian Challenge" : {
        "Image" : 'src/data/card_images/KSE/Cards/guardianChallenge.png',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Guardian,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "Ranger Challenge" : {
        "Image" : 'src/data/card_images/KSE/Cards/rangerChallenge.png',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Ranger,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "Thief Challenge" : {
        "Image" : 'src/data/card_images/KSE/Cards/thiefChallenge.png',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Thief,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "Wizard Challenge" : {
        "Image" : 'src/data/card_images/KSE/Cards/wizardChallenge.png',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Sorcerer,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "Druid Challenge" : {
        "Image" : '',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Druid,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "Warrior Challenge" : {
        "Image" : '',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Warrior,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "Berserker Challenge" : {
        "Image" : '',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Berserker,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "Necromancer Challenge" : {
        "Image" : '',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Necromancer,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "Sorcerer Challenge" : {
        "Image" : '',
        "Effect" : cardEffect.Challenge,
        "Requirement" : heroType.Sorcerer,
        "Card Type"   : cardType.Action,
        "Description" : "You may play this card when another player attempts to play a Hero, Item, or Magic card. CHALLENGE that card. +3 to your roll"
    },
    "+4 Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.OneModifier,
        "Positive Effect" : 4,
        "Quantity" : 4,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +4 to that roll."
    },
    "+3/-1 Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Modifier,
        "Positive Effect" : 3,
        "Negative Effect" : 1,
        "Quantity" : 4,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +3 or -1 to that roll."
    },
    "+2/-2 Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Modifier,
        "Positive Effect" : 2,
        "Negative Effect" : 2,
        "Quantity" : 9,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +2 or -2 to that roll."
    },
    "+1/-3 Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Modifier,
        "Positive Effect" : 1,
        "Negative Effect" : 3,
        "Quantity" : 4,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +1 or -3 to that roll."
    },
    "-4 Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.OneModifier,
        "Negative Effect" : 4,
        "Quantity" : 4,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. -4 to that roll."
    },
    #Warriors and Druids Modifiers
    "+1/-1 WaD Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Draw2Modifier,
        "Positive Effect" : 1,
        "Negative Effect" : 1,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +1 or -1 to that roll. DRAW 2 cards."
    },
    "+2/-1 WaD Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Draw1Modifier,
        "Positive Effect" : 2,
        "Negative Effect" : 1,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +2 or -1 to that roll. DRAW a card."
    },
    "+4 WaD Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.DrawIfAboveModifier,
        "Positive Effect" : 4,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +1 or -1 to that roll. If the roll is modified above 12, DRAW a card."
    },
    "-4 WaD Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.SearchDiscBelowMod,
        "Negative Effect" : 4,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +4 that roll. If the roll is modified below 2, choose a card from the discard pile and add it to your hand."
    },
    #Berserkers and Necromancers Modifiers
    "+2/-2 BaN Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.AtkBonusModifier,
        "Positive Effect" : 2,
        "Negative Effect" : 2,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +2 or -2 to that roll. If you are attacking a Monster card, +4 to that roll instead."
    },
    "+7 BaN Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.DiscardHandModifier,
        "Positive Effect" : 7,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. DISCARD your hand. +7 to that roll. "
    },
    #Dragon Sorcerers Modifiers
    "+6 DS Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Discard1Modifier,
        "Positive Effect" : 6,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice and DISCARD a card. +6 to that roll."
    },
    "-6 DS Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Discard1Modifier,
        "Negative Effect" : 6,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice and DISCARD a card. -6 to that roll"
    },
    #KSE Modifiers
    "+1/-4 KSE Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Modifier,
        "Positive Effect" : 1,
        "Negative Effect" : 4,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +1 or -4 to that roll."
    },
    "+2/-3 KSE Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Modifier,
        "Positive Effect" : 2,
        "Negative Effect" : 3,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +2 or -3 to that roll."
    },
    "+3/-2 KSE Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Modifier,
        "Positive Effect" : 3,
        "Negative Effect" : 2,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +3 or -2 to that roll."
    },
    "+4/-1 KSE Modifier" : {
        "Image" : '',
        "Effect" : cardEffect.Modifier,
        "Positive Effect" : 4,
        "Negative Effect" : 1,
        "Card Type"   : cardType.Action,
        "Description" : "Play this card after any player (including you) rolls the dice. +4 or -1 to that roll."
    },
#Magic
    "Call to the Fallen" : {
        "Image" : '',
        "Effect" : cardEffect.CallToTheFallen,
        "Card Type"   : cardType.Magic,
        "Description" : "Search the discard pile for a Hero card and add it to your hand."
    },
    "Critical Boost" : {
        "Image" : '',
        "Effect" : cardEffect.CriticalBoost,
        "Quantity"    : 2,
        "Card Type"   : cardType.Magic,
        "Description" : "DRAW 3 cards and DISCARD a card."
    },
    "Destructive Spell" : {
        "Image" : '',
        "Effect" : cardEffect.DestructiveSpell,
        "Quantity"    : 2,
        "Card Type"   : cardType.Magic,
        "Description" : "DISCARD a card, then DESTROY a Hero card."
    },
    "Enchanted Spell" : {
        "Image" : '',
        "Effect" : cardEffect.EnchantedSpell,
        "Quantity"    : 2,
        "Card Type"   : cardType.Magic,
        "Description" : "+2 to all of your rolls until the end of your turn."
    },
    "Entangling Trap" : {
        "Image" : '',
        "Effect" : cardEffect.EnchantedSpell,
        "Quantity"    : 2,
        "Card Type"   : cardType.Magic,
        "Description" : "DISCARD 2 cards, then STEAL a Hero card."
    },
    "Forced Exchange" : {
        "Image" : '',
        "Effect" : cardEffect.ForcedExchange,
        "Card Type"   : cardType.Magic,
        "Description" : "Choose a player. STEAL a Hero card from that player's Party, then move a Hero card from your Party to that player's Party.",
        "Ranked Description" : "Choose a player. TRADE Heroes with that player."
    },
    "Forecful Winds" : {
        "Image" : '',
        "Effect" : cardEffect.ForcefulWinds,
        "Card Type"   : cardType.Magic,
        "Description" : "Return every equipped Item card to its respective player's hand."
    },
    "Winds of Change" : {
        "Image" : '',
        "Effect" : cardEffect.WindsOfChange,
        "Quantity"    : 2,
        "Card Type"   : cardType.Magic,
        "Description" : "Return an Item card equipped to any player's Hero card to that player's hand, then DRAW a card."
    },
    #Warriors and Druids Magic
    "Beast Call" : {
        "Image" : '',
        "Effect" : cardEffect.BeastCall,
        "Card Type"   : cardType.Magic,
        "Description" : "Move all face-up Monster cards to the bottom of the Monster deck and flip the top 3 cards from the Monster deck face up. You may spend an extra action point this turn."
    },
    "Rapid Refresh" : {
        "Image" : '',
        "Effect" : cardEffect.RapidRefresh,
        "Card Type"   : cardType.Magic,
        "Description" : "DISCARD every card in your hand (if you have any) and DRAW 4 cards.",
        "Ranked Description" : "DISCARD every card in your hand and DRAW 4 cards."
    },
    #Berserkers and Necromancers Magic
    "Lightning Labrys" : {
        "Image" : '',
        "Effect" : cardEffect.LightningLabrys,
        "Quantity"    : 2,
        "Card Type"   : cardType.Magic,
        "Description" : "DISCARD up to 3 cards. For each card discarded, choose a player. That player must SACRIFICE a Hero card."
    },
    "Mass Sacrifice" : {
        "Image" : '',
        "Effect" : cardEffect.MassSacrifice,
        "Quantity"    : 2,
        "Card Type"   : cardType.Magic,
        "Description" : "DISCARD your hand, then DRAW 5 cards."
    },
    #Dragon Sorcerers Magic
    "Egg of Fortune" : {
        "Image" : '',
        "Effect" : cardEffect.EggOfFortune,
        "Card Type"   : cardType.Magic,
        "Description" : "DISCARD a card, then pull a card from each other player's hand."
    },
    #KSE Magic
    "Capitvating Spell" : {
        "Image" : '',
        "Effect" : cardEffect.CapitvatingSpell,
        "Card Type"   : cardType.Magic,
        "Description" : "+3 to all of your rolls until the end of your turn"
    },
#Items
    #Masks
    "Bard Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Bard instead of its original class."
    },
    "Fighter Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Fighter instead of its original class."
    },
    "Guardian Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Guardian instead of its original class."
    },
    "Ranger Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Ranger instead of its original class."
    },
    "Thief Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Thief instead of its original class."
    },
    "Wizard Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Wizard instead of its original class."
    },
    "Druid Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Druid instead of its original class."
    },
    "Warrior Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Warrior instead of its original class."
    },
    "Berserker Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Berserker instead of its original class."
    },
    "Necromancer Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Necromancer instead of its original class."
    },
    "Sorcerer Mask" : {
        "Image" : '',
        "Mask" : True,
        "Effect" : cardEffect.Mask,
        "Card Type"   : cardType.Item,
        "Description" : "The equipped Hero card is considered a Sorcerer instead of its original class."
    },
    #Base Game Items
    "Decoy Doll" : {
        "Image" : '',
        "Effect" : cardEffect.DecoyDoll,
        "Card Type"   : cardType.Item,
        "Description" : "If the equipped Hero card would be sacrificed or destroyed, move this card to the discard pile instead."
    },
    "Particularly Rusty Coin" : {
        "Image" : '',
        "Effect" : cardEffect.ParticularlyRustyCoin,
        "Quantity"    : 2,
        "Card Type"   : cardType.Item,
        "Description" : "If you unsuccessfully roll to use the equipped Hero card's effect, DRAW a card."
    },
    "Really Big Ring" : {
        "Image" : '',
        "Effect" : cardEffect.ReallyBigRing,
        "Quantity"    : 2,
        "Card Type"   : cardType.Item,
        "Description" : "Each time you roll to use the equipped Hero card's effect, +2 to your roll."
    },
    #Warriors and Druids Items
    "Bottomless Bag" : {
        "Image" : '',
        "Effect" : cardEffect.BottomlessBag,
        "Card Type"   : cardType.Item,
        "Description" : "You may roll to use the equipped Hero card's effect more than once per turn, at a cost of one action point for each roll to use."
    },
    "Even Bigger Ring" : {
        "Image" : '',
        "Effect" : cardEffect.EvenBiggerRing,
        "Card Type"   : cardType.Item,
        "Description" : "Each time you roll to use the equipped Hero card's effect, +4 to your roll."
    },
    "Temporal Hourglass" : {
        "Image" : '',
        "Effect" : cardEffect.TemporalHourglass,
        "Card Type"   : cardType.Item,
        "Description" : "If you unsuccessfully roll to use the equipped Hero card's effect, you may spend an extra action point this turn."
    },
    #Berserkers and Necromancers Items
    "Biggest Ring Ever" : {
        "Image" : '',
        "Effect" : cardEffect.BiggestRingEver,
        "Card Type"   : cardType.Item,
        "Description" : "Each time you roll to use the equipped Hero card's effect, you may DISCARD up to 3 cards. For each card discarded, +2 to your roll."
    },
    "Goblet of Caffeination" : {
        "Image" : '',
        "Effect" : cardEffect.GobletOfCaffeination,
        "Card Type"   : cardType.Item,
        "Description" : "If you unsuccessfully roll to use the equipped Hero card's effect, you may SACRIFICE this card, then roll to use that effect again immediately."
    },
    "Silver Lining" : {
        "Image" : '',
        "Effect" : cardEffect.SilverLining,
        "Card Type"   : cardType.Item,
        "Description" : "If you unsuccessfully roll to use the equipped Hero card's effect, +2 to all of your rolls for the rest of your turn."
    },
    #KSE Items
    "Mysterious Feather" : {
        "Image" : '',
        "Effect" : cardEffect.MysteriousFeather,
        "Card Type"   : cardType.Item,
        "Description" : "Each time you roll to use this Hero card's effect, you may DISCARD a card. If you do, +3 to your roll."
    },
    
    #Base Game Curses
    "Curse of the Snake's Eyes" : {
        "Image" : '',
        "Curse" : True,
        "Effect" : cardEffect.CurseOfTheSnakesEyes,
        "Quantity"    : 2,
        "Card Type"   : cardType.Item,
        "Description" : "Each time you roll to use the equipped Hero card's effect, -2 to your roll."
    },
    "Sealing Key" : {
        "Image" : '',
        "Curse" : True,
        "Card Type"   : cardType.Item,
        "Effect" : cardEffect.SealingKey,
        "Description" : "You cannot use the equipped Hero card's effect."
    },
    "Suspiciously Shiny Coin" : {
        "Image" : '',
        "Curse" : True,
        "Effect" : cardEffect.SuspiciouslyShinyCoin,
        "Card Type"   : cardType.Item,
        "Description" : "If you successfully roll to use the equipped Hero Card's effect, DISCARD a card."
    },
    #Warriors and Druids Curses
    "Cursed Glove" : {
        "Image" : '',
        "Curse" : True,
        "Effect" : cardEffect.CursedGlove,
        "Card Type"   : cardType.Item,
        "Description" : "If another Hero card in your Party is stolen, move the equipped Hero card to the Party of the player who stole it as well."
    },
    "Soul Tether" : {
        "Image" : '',
        "Curse" : True,
        "Effect" : cardEffect.SoulTether,
        "Card Type"   : cardType.Item,
        "Description" : "If any Hero card in your Party is sacrificed for destroyed, SACRIFICED the equipped Hero card."
    },
    #Berserkers and Necromancers Curses
    "Dragon's Bile" : {
        "Image" : '',
        "Curse" : True,
        "Effect" : cardEffect.DragonsBile,
        "Card Type"   : cardType.Item,
        "Description" : "If you unsuccessfully roll to use the equipped Hero card's effect, SACRIFICE a Hero card."
    },
    "Soulbound Grimoire" : {
        "Image" : '',
        "Curse" : True,
        "Effect" : cardEffect.SoulboundGrimoire,
        "Card Type"   : cardType.Item,
        "Description" : "Rolling to use the equipped Hero card's effect costs 2 action points."
    },
    #KSE Curses
    "Mask of Misfortune" : {
        "Image" : '',
        "Curse" : True,
        "Effect" : cardEffect.MaskOfMisfortune,
        "Card Type"   : cardType.Item,
        "Description" : "This Hero card has no class."
    },
    #Banner Quest Curses
    "Chaos Mask" : {
        "Image" : '',
        "Curse" : True,
        "Effect" : cardEffect.NoEffect,
        "Card Type"   : cardType.Item,
        "Description" : "Unknown"
    },
    "Morph Mask" : {
        "Image" : '',
        "Curse" : True,
        "Effect" : cardEffect.NoEffect,
        "Card Type"   : cardType.Item,
        "Description" : "Unknown"
    },
#Heroes
    "None" : {
        "Image" : '',
        "Description" : "Temporary placeholder for src/active_player.py"
    },
    "Bad Axe" : {
        "Image" : '',
        "Class" : heroType.Fighter,
        "Effect" : cardEffect.BadAxe,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "DESTROY a Hero card."
    },
    "Bear Claw" : {
        "Image" : '',
        "Class" : heroType.Fighter,
        "Effect" : cardEffect.PullCard,
        "Pull Type" : cardType.Hero,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Pull a card from another player's hand. If it is a Hero card, pull a second card from that player's hand."
    },
    "Beary Wise" : {
        "Image" : '',
        "Class" : heroType.Fighter,
        "Effect" : cardEffect.BearyWise,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Each other player must DISCARD a card. Choose one of the discarded cards and add it to your hand."
    },
    "Fury Knuckle" : {
        "Image" : '',
        "Class" : heroType.Fighter,
        "Effect" : cardEffect.PullCard,
        "Pull Type" : cardType.Challenge,
        "Effect Roll" : 5,
        "Card Type"   : cardType.Hero,
        "Description" : "Pull a card from another player's hand. If it is a Challenge card, pull a second card from that player's hand."
    },
    "Heavy Bear" : {
        "Image" : '',
        "Class" : heroType.Fighter,
        "Effect" : cardEffect.ForceDiscard,
        "Effect Roll" : 5,
        "Card Type"   : cardType.Hero,
        "Description" : "Choose a player. That player must DISCARD 2 cards."
    },
    "Pan Chucks" : {
        "Image" : '',
        "Class" : heroType.Fighter,
        "Effect" : cardEffect.PanChucks,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW 2 cards. If at least one of those cards is a Challenge card, you may reveal it, then DESTROY a Hero card."
    },
    "Qi Fighter" : {
        "Class" : heroType.Fighter,
        "Effect" : cardEffect.QiBear,
        "Effect Roll" : 10,
        "Card Type"   : cardType.Hero,
        "Description" : "DISCARD up to 3 cards. For each card discarded, DESTROY a Hero card."
    },
    "Tough Teddy" : {
        "Image" : '',
        "Class" : heroType.Fighter,
        "Effect" : cardEffect.ToughTeddy,
        "Effect Roll" : 4,
        "Card Type"   : cardType.Hero,
        "Description" : "Each other player with a Fighter in their Party must DISCARD a card."
    },
    "Dodgy Dealer" : {
        "Image" : '',
        "Class" : heroType.Bard,
        "Effect" : cardEffect.DodgyDealer,
        "Effect Roll" : 9,
        "Card Type"   : cardType.Hero,
        "Description" : "Trade hands with another player."
    },
    "Fuzzy Cheeks" : {
        "Image" : '',
        "Class" : heroType.Bard,
        "Effect" : cardEffect.FuzzyCheeks,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW a card and play a Hero card from your hand immediately."
    },
    "Greedy Cheeks" : {
        "Image" : '',
        "Class" : heroType.Bard,
        "Effect" : cardEffect.GreedyCheeks,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "Each other player must give you a card from their hand." #If they can
    },
    "Lucky Bucky" : {
        "Image" : '',
        "Class" : heroType.Bard,
        "Effect" : cardEffect.LuckyBucky,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Pull a card from another player's hand. If that card is a Hero card, you may play it immediately."
    },
    "Mellow Dee" : {
        "Image" : '',
        "Class" : heroType.Bard,
        "Effect" : cardEffect.MellowDee,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW a card. If that card is a Hero card, you may play it immediately."
    },
    "Napping Nibbles" : {
        "Image" : '',
        "Class" : heroType.Bard,
        "Effect" : cardEffect.NoEffect,
        "Effect Roll" : 2,
        "Card Type"   : cardType.Hero,
        "Description" : "Do nothing."
    },
    "Peanut" : {
        "Image" : '',
        "Class" : heroType.Bard,
        "Effect" : cardEffect.Draw2,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW 2 cards."
    },
    "Tipsy Tootie" : {
        "Image" : '',
        "Class" : heroType.Bard,
        "Effect" : cardEffect.TipsyTootie,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "Choose a player. STEAL a Hero card from that player's Party and move this card to that player's Party."
    },
    "Calming Voice" : {
        "Image" : '',
        "Class" : heroType.Guardian,
        "Effect" : cardEffect.CalmingVoice,
        "Effect Roll" : 9,
        "Card Type"   : cardType.Hero,
        "Description" : "Hero cards in your Party cannot be stolen until your next turn."
    },
    "Guiding Light" : {
        "Image" : '',
        "Class" : heroType.Guardian,
        "Effect" : cardEffect.SearchDiscard,
        "Search Target" : cardType.Hero,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Search the discard pile for a Hero card and add it to your hand."
    },
    "Holy Curselifter" : {
        "Image" : '',
        "Class" : heroType.Guardian,
        "Effect" : cardEffect.HolyCurselifter,
        "Effect Roll" : 5,
        "Card Type"   : cardType.Hero,
        "Description" : "Return a Cursed Item card equipped to a Hero card in your Party to your hand."
    },
    "Iron Resolve" : {
        "Image" : '',
        "Class" : heroType.Guardian,
        "Effect" : cardEffect.IronResolve,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "Cards you play cannot be challenged for the rest of your turn."
    },
    "Mighty Blade" : {
        "Image" : '',
        "Class" : heroType.Guardian,
        "Effect" : cardEffect.MightyBlade,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "Hero cards in your Party cannot be destroyed until your next turn."
    },
    "Radiant Horn" : {
        "Image" : '',
        "Class" : heroType.Guardian,
        "Effect" : cardEffect.SearchDiscard,
        "Search Target" : cardType.Hero,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "Search the discard pile for a Modifier card and add it to your hand"
    },
    "Vibrant Glow" : {
        "Image" : '',
        "Class" : heroType.Guardian,
        "Effect" : cardEffect.VibrantGlow,
        "Effect Roll" : 9,
        "Card Type"   : cardType.Hero,
        "Description" : "+5 to all of your rolls until the end of your turn."
    },
    "Wise Shield" : {
        "Image" : '',
        "Class" : heroType.Guardian,
        "Effect" : cardEffect.WiseShield,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "+3 to all of your rolls until the end of your turn."
    },
    "Bullseye" : {
        "Image" : '',
        "Class" : heroType.Ranger,
        "Effect" : cardEffect.Bullseye,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Look at the top 3 cards of the deck. Add one to your hand, then return the other two to the top of the deck in any order."
    },
    "Hook" : {
        "Image" : '',
        "Class" : heroType.Ranger,
        "Effect" : cardEffect.Hook,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "Play an Item card from your hand immediately and DRAW a card."
    },
    "Lookie Rookie" : {
        "Image" : '',
        "Class" : heroType.Ranger,
        "Effect" : cardEffect.SearchDiscard,
        "Search Target" : cardType.Item,
        "Effect Roll" : 5,
        "Card Type"   : cardType.Hero,
        "Description" : "Search the discard pile for an Item card and add it to your hand."
    },
    "Quick Draw" : {
        "Image" : '',
        "Class" : heroType.Ranger,
        "Effect" : cardEffect.QuickDraw,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "Draw 2 cards. If at least one of those cards is an Item card, you may play one of them immediately."
    },
    "Serious Grey" : {
        "Image" : '',
        "Class" : heroType.Ranger,
        "Effect" : cardEffect.SeriousGrey,
        "Effect Roll" : 9,
        "Card Type"   : cardType.Hero,
        "Description" : "DESTROY a Hero card and DRAW a card."
    },
    "Sharp Fox" : {
        "Image" : '',
        "Class" : heroType.Ranger,
        "Effect" : cardEffect.SharpFox,
        "Effect Roll" : 5,
        "Card Type"   : cardType.Hero,
        "Description" : "Look at another player's hand."
    },
    "Wildshot" : {
        "Image" : '',
        "Class" : heroType.Ranger,
        "Effect" : cardEffect.Wildshot,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW 3 cards and DISCARD a card."
    },
    "Wily Red" : {
        "Image" : '',
        "Class" : heroType.Ranger,
        "Effect" : cardEffect.WilyRed,
        "Effect Roll" : 10,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW cards until you have 7 cards in your hand."
    },
    "Kit Napper" : {
        "Image" : '',
        "Class" : heroType.Thief,
        "Effect" : cardEffect.StealHero,
        "Effect Roll" : 9,
        "Card Type"   : cardType.Hero,
        "Description" : "STEAL a Hero card."
    },
    "Meowzio" : {
        "Image" : '',
        "Class" : heroType.Thief,
        "Effect" : cardEffect.Meowzio,
        "Effect Roll" : 10,
        "Card Type"   : cardType.Hero,
        "Description" : "Choose a player. STEAL a Hero card from that player's Party and pull a card from that player's hand."
    },
    "Plundering Puma" : {
        "Image" : '',
        "Class" : heroType.Thief,
        "Effect" : cardEffect.PlunderingPuma,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "Pull 2 cards from another player's hand. That player may DRAW a card."
    },
    "Shurikitty" : {
        "Image" : '',
        "Class" : heroType.Thief,
        "Effect" : cardEffect.Shurikitty,
        "Effect Roll" : 9,
        "Card Type"   : cardType.Hero,
        "Description" : "DESTROY a Hero card. If that Hero card had an item card equipped to it, add that item card to your hand instead of moving it to the discard pile."
    },
    "Silent Shadow" : {
        "Image" : '',
        "Class" : heroType.Thief,
        "Effect" : cardEffect.SilentShadow,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "Look at another player's hand. Choose a card and add it to your hand."
    },
    "Slippery Paws" : {
        "Image" : '',
        "Class" : heroType.Thief,
        "Effect" : cardEffect.SlipperyPaws,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "Pull 2 cards from another player's hand, then DISCARD one of those cards."
    },
    "Sly Pickings" : {
        "Image" : '',
        "Class" : heroType.Thief,
        "Effect" : cardEffect.PullAndPlay,
        "Search Target" : cardType.Item,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "Pull a card from another player's hand. If that card is an item card, you may play it immediately."
    },
    "Smooth Mimimeow" : {
        "Image" : '',
        "Class" : heroType.Thief,
        "Effect" : cardEffect.SmoothMimimeow,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Pull a card from the hand of each other player with a Thief in their Party."
    },
    "Bun Bun" : {
        "Image" : '',
        "Class" : heroType.Wizard,
        "Effect" : cardEffect.BunBun,
        "Effect Roll" : 5,
        "Card Type"   : cardType.Hero,
        "Description" : "Search the discard pile for a Magic card and add it to your hand."
    },
    "Buttons" : {
        "Image" : '',
        "Class" : heroType.Wizard,
        "Effect" : cardEffect.PullAndPlay,
        "Search Target" : cardType.Magic,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "Pull a card from another player's hand. If it is a Magic card, you may play it immediately."
    },
    "Fluffy" : {
        "Image" : '',
        "Class" : heroType.Wizard,
        "Effect" : cardEffect.Fluffy,
        "Effect Roll" : 10,
        "Card Type"   : cardType.Hero,
        "Description" : "DESTROY 2 Hero cards."
    },
    "Hopper" : {
        "Image" : '',
        "Class" : heroType.Wizard,
        "Effect" : cardEffect.Hopper,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Choose a player. That player must SACRIFICE a Hero card."
    },
    "Snowball" : {
        "Image" : '',
        "Class" : heroType.Wizard,
        "Effect" : cardEffect.Snowball,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW a card. If it is a Magic card, you may play it immediately and DRAW a second card."
    },
    "Spooky" : {
        "Image" : '',
        "Class" : heroType.Wizard,
        "Effect" : cardEffect.Spooky,
        "Effect Roll" : 10,
        "Card Type"   : cardType.Hero,
        "Description" : "Each other player must SACRIFICE a Hero card."
    },
    "Whiskers" : {
        "Image" : '',
        "Class" : heroType.Wizard,
        "Effect" : cardEffect.Whiskers,
        "Effect Roll" : 11,
        "Card Type"   : cardType.Hero,
        "Description" : "STEAL a Hero card and DESTROY a Hero card."
    },
    "Wiggles" : {
        "Image" : '',
        "Class" : heroType.Wizard,
        "Effect" : cardEffect.Wiggles,
        "Effect Roll" : 10,
        "Card Type"   : cardType.Hero,
        "Description" : "STEAL a Hero and roll to use its effect immediately"
    },
    #Warriors and Druids
    "Big Buckley" : {
        "Image" : '',
        "Class" : heroType.Druid,
        "Effect" : cardEffect.BigBuckley,
        "Effect Roll" : 8,
        "Negative Roll" : True,
        "Card Type"   : cardType.Hero,
        "Description" : "ATTACK a Monster card immediately. (You must still meet its Party requirement.)"
    },
    "Buck Omens" : {
        "Image" : '',
        "Class" : heroType.Druid,
        "Effect" : cardEffect.BuckOmens,
        "Effect Roll" : 6,
        "Negative Roll" : True,
        "Card Type"   : cardType.Hero,
        "Description" : "Look at another player's hand. Choose a Hero card from their hand (if they have one) and bring it into your Party."
    },
    "Doe Fallow" : {
        "Image" : '',
        "Class" : heroType.Druid,
        "Effect" : cardEffect.DoeFallow,
        "Effect Roll" : 7,
        "Negative Roll" : True,
        "Card Type"   : cardType.Hero,
        "Description" : "SACRIFICE a Hero card, then DRAW cards until you have 7 cards in your hand."
    },
    "Glowing Antler" : {
        "Image" : '',
        "Class" : heroType.Druid,
        "Effect" : cardEffect.Play2,
        "Search Target" : cardType.Magic,
        "Effect Roll" : 7,
        "Negative Roll" : True,
        "Card Type"   : cardType.Hero,
        "Description" : "You may play up to 2 Magic cards immediately."
    },
    "Maegisty" : {
        "Image" : '',
        "Class" : heroType.Druid,
        "Effect" : cardEffect.Maegisty,
        "Effect Roll" : 7,
        "Negative Roll" : True,
        "Card Type"   : cardType.Hero,
        "Description" : "Until your next turn, if a Hero card in your Party would be sacrificed or destroyed, return it to your hand instead."
    },
    "Magus Moose" : {
        "Image" : '',
        "Class" : heroType.Druid,
        "Effect" : cardEffect.MagusMoose,
        "Effect Roll" : 5,
        "Negative Roll" : True,
        "Card Type"   : cardType.Hero,
        "Description" : "Search the discard pile for a Hero card and add it to your hand, then play it immediately."
    },
    "Majestelk" : {
        "Image" : '',
        "Class" : heroType.Druid,
        "Effect" : cardEffect.Majestelk,
        "Effect Roll" : 7,
        "Negative Roll" : True,
        "Card Type"   : cardType.Hero,
        "Description" : "SACRIFICE a Hero card. +5 or -5 to each of your rolls until your next turn."
    },
    "Stagguard" : {
        "Image" : '',
        "Class" : heroType.Druid,
        "Effect" : cardEffect.Stagguard,
        "Effect Roll" : 8,
        "Negative Roll" : True,
        "Card Type"   : cardType.Hero,
        "Description" : "No other player can play Modifier cards until the end of your turn."
    },
    "Agile Dagger" : {
        "Image" : '',
        "Class" : heroType.Warrior,
        "Effect" : cardEffect.Play2,
        "Search Target" : cardType.Item,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "You may play up to 2 Item cards immediately."
    },
    "Blinding Blade" : {
        "Image" : '',
        "Class" : heroType.Warrior,
        "Effect" : cardEffect.BlindingBlade,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "Choose any player. Return all equipped Item cards in that player's Party to your hand."
    },
    "CriticalFang" : {
        "Image" : '',
        "Class" : heroType.Warrior,
        "Effect" : cardEffect.CriticalFang,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "+4 to your rolls to ATTACK a Monster card until the end of your turn."
    },
    "Hardened Hunter" : {
        "Image" : '',
        "Class" : heroType.Warrior,
        "Effect" : cardEffect.HardenedHunter,
        "Effect Roll" : 9,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW a card for each Monster card in each other player's Party."
    },
    "Looting Lupo" : {
        "Image" : '',
        "Class" : heroType.Warrior,
        "Effect" : cardEffect.LootingLupo,
        "Effect Roll" : 5,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW a card for each Item card equipped to a Hero card in your Party."
    },
    "Silent Shield" : {
        "Image" : '',
        "Class" : heroType.Warrior,
        "Effect" : cardEffect.SilentShield,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "For the rest of your turn, if you SACRIFICE or DESTROY a Hero card, you may search the discard pile for a Hero card and add it to your hand."
    },
    "Tenacious Timber" : {
        "Image" : '',
        "Class" : heroType.Warrior,
        "Effect" : cardEffect.TenaciousTimber,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "For each Monster card in your Party, STEAL a Hero."
    },
    "Wolfgang Pack" : {
        "Image" : '',
        "Class" : heroType.Warrior,
        "Effect" : cardEffect.WolfgangPack,
        "Effect Roll" : 5,
        "Card Type"   : cardType.Hero,
        "Description" : "For each other Hero card in your party, +1 to all of your rolls until the end of your turn."
    },
    #Berserkers and Necromancers
    "Bark Hexer" : {
        "Image" : '',
        "Class" : heroType.Necromancer,
        "Effect" : cardEffect.BarkHexer,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "DISCARD a card. Each other player must DISCARD 2 cards."
    },
    "Beholden Retriever" : {
        "Image" : '',
        "Class" : heroType.Necromancer,
        "Effect" : cardEffect.BeholdenRetriever,
        "Effect Roll" : 5,
        "Card Type"   : cardType.Hero,
        "Description" : "SACRIFICE a Hero card. Search the discard pile for a Hero or Item card and add it to your hand, then play it immediately."
    },
    "Bone Collector" : {
        "Image" : '',
        "Class" : heroType.Necromancer,
        "Effect" : cardEffect.BoneCollector,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "SACRIFICE an Item card. Search the discard pile for a Hero card and add it to your hand, then play it immediately."
    },
    "Boston Terror" : {
        "Image" : '',
        "Class" : heroType.Necromancer,
        "Effect" : cardEffect.BostonTerror,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Choose a player. That player may give you a card from their hand. If they do not, you may choose 2 cards from the discard pile and add them to your hand."
    },
    "Grim Pupper" : {
        "Image" : '',
        "Class" : heroType.Necromancer,
        "Effect" : cardEffect.GrimPupper,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "Each player (including you) must SACRIFICE a card."
    },
    "Hollow Husk" : {
        "Image" : '',
        "Class" : heroType.Necromancer,
        "Effect" : cardEffect.HollowHusk,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "Look at another player's hand. Choose a Magic card (if they have one) and add it to your hand. You may play it immediately."
    },
    "Perfect Vessel" : {
        "Image" : '',
        "Class" : heroType.Necromancer,
        "Effect" : cardEffect.PerfectVessel,
        "Effect Roll" : 4,
        "Card Type"   : cardType.Hero,
        "Description" : "SACRIFICE this card, then STEAL a Hero card."
    },
    "Shadow Saint" : {
        "Image" : '',
        "Class" : heroType.Necromancer,
        "Effect" : cardEffect.ShadowSaint,
        "Effect Roll" : 5,
        "Card Type"   : cardType.Hero,
        "Description" : "DISCARD a Modifier card. No other player can play Modifier cards until the end of your turn."
    },
    "Annihilator" : {
        "Image" : '',
        "Class" : heroType.Berserker,
        "Effect" : cardEffect.Annihilator,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "Search the discard pile for a Challenge card and add it to your hand."
    },
    "Brawling Spirit" : {
        "Image" : '',
        "Class" : heroType.Berserker,
        "Effect" : cardEffect.BrawlingSpirit,
        "Effect Roll" : 9,
        "Card Type"   : cardType.Hero,
        "Description" : "Each player (including you) with more than 3 cards in their Party must SACRIFICE a card"
    },
    "Gruesome Gladiator" : {
        "Image" : '',
        "Class" : heroType.Berserker,
        "Effect" : cardEffect.GruesomeGladiator,
        "Effect Roll" : 10,
        "Card Type"   : cardType.Hero,
        "Description" : "Look at each other player's hand. Choose a card from each player's hand and add it to your hand."
    },
    "Meowntain" : {
        "Image" : '',
        "Class" : heroType.Berserker,
        "Effect" : cardEffect.Meowntain,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "SACRIFICE a card. +5 to all of your rolls until the end of your turn."
    },
    "Rabid Beast" : {
        "Image" : '',
        "Class" : heroType.Berserker,
        "Effect" : cardEffect.RabidBeast,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "SACRIFICE any number of cards, then DESTROY the same number of cards."
    },
    "Roaryal Guard" : {
        "Image" : '',
        "Class" : heroType.Berserker,
        "Effect" : cardEffect.RoaryalGuard,
        "Effect Roll" : 9,
        "Card Type"   : cardType.Hero,
        "Description" : "Choose a Class. Return every Hero card of that Class to its respective player's hand."
    },
    "Vicious Wildcat" : {
        "Image" : '',
        "Class" : heroType.Berserker,
        "Effect" : cardEffect.ViciousWildcat,
        "Effect Roll" : 12,
        "Card Type"   : cardType.Hero,
        "Description" : "SLAY any Monster card, then end your turn."
    },
    "Unbridled Fury" : {
        "Image" : '',
        "Class" : heroType.Berserker,
        "Effect" : cardEffect.UnbridledFury,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "DESTROY a Hero card. If that Hero card is a Berserker, you may spend an extra action point this turn."
    },
    "Dragalter" : {
        "Image" : '',
        "Class" : heroType.Sorcerer,
        "Effect" : cardEffect.Dragalter,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "DISCARD a Modifier card. You may apply that Modifier card's effect to all of your rolls for the rest of this turn."
    },
    "Dystortivern" : {
        "Image" : '',
        "Class" : heroType.Sorcerer,
        "Effect" : cardEffect.Dystortivern,
        "Effect Roll" : 10,
        "Card Type"   : cardType.Hero,
        "Description" : "Trade Party Leader cards with another player."
    },
    "Extraga" : {
        "Image" : '',
        "Class" : heroType.Sorcerer,
        "Effect" : cardEffect.Extraga,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Each player (including you) must return any other Sorcerers in their Party to their hand."
    },
    "Luut" : {
        "Image" : '',
        "Class" : heroType.Sorcerer,
        "Effect" : cardEffect.Luut,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "STEAL an Item card and equip it to a Hero card in your Party."
    },
    "Mirroryu" : {
        "Image" : '',
        "Class" : heroType.Sorcerer,
        "Effect" : cardEffect.Mirroryu,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Roll to use the effect of any Hero card in your Party immediately. +3 to that roll."
    },
    "Oracon" : {
        "Image" : '',
        "Class" : heroType.Sorcerer,
        "Effect" : cardEffect.Oracon,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Pull a card from another player's hand. If it is a Modifier card, that player must SACRIFICE a Hero card."
    },
    "Renovern" : {
        "Image" : '',
        "Class" : heroType.Sorcerer,
        "Effect" : cardEffect.Renovern,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "Search the discard pile for an item card and play it immediately."
    },
    "Shamanaga" : {
        "Image" : '',
        "Class" : heroType.Sorcerer,
        "Effect" : cardEffect.Shamanaga,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Choose a Hero card from the discard pile. Bring that Hero card into your Party, roll to use its effect immediately, then SACRIFICE it."
    },
    "Smok" : {
        "Image" : '',
        "Class" : heroType.Sorcerer,
        "Effect" : cardEffect.Smok,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW 2 cards. If at least one of those cards is a Magic card, you may reveal it, then spend an extra action point this turn."
    },
    #KSE
    "Hamlet" : {
        "Image" : '',
        "Class" : heroType.Bard,
        "Effect" : cardEffect.Hamlet,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Each player (including you) must return any other Bards in their Party to their hand."
    },
    "Bearserker" : {
        "Image" : '',
        "Class" : heroType.Fighter,
        "Effect" : cardEffect.Bearserker,
        "Effect Roll" : 6,
        "Card Type"   : cardType.Hero,
        "Description" : "Choose any player. That player must DISCARD all cards in their hand and DRAW 3 cards."
    },
    "Complex Illusion" : {
        "Image" : '',
        "Class" : heroType.Guardian,
        "Effect" : cardEffect.ComplexIllusion,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "DRAW 2 cards. If at least one of those cards is a Modifier card, you may reveal it, then spend an extra action point this turn."
    },
    "Enchantler" : {
        "Image" : '',
        "Class" : heroType.Druid,
        "Effect" : cardEffect.Enchantler,
        "Effect Roll" : 7,
        "Negative Roll" : True,
        "Card Type"   : cardType.Hero,
        "Description" : "DISCARD any number of cards. +2 to all of your rolls for the rest of your turn for each card discarded."
    },
    "Hoodwink" : {
        "Image" : '',
        "Class" : heroType.Ranger,
        "Effect" : cardEffect.Hoodwink,
        "Effect Roll" : 8,
        "Card Type"   : cardType.Hero,
        "Description" : "Swap the item cards equipped to any 2 Hero cards."
    },
    "Purring Bandit" : {
        "Image" : '',
        "Class" : heroType.Thief,
        "Effect" : cardEffect.PurringBandit,
        "Effect Roll" : 7,
        "Card Type"   : cardType.Hero,
        "Description" : "Pull a card from each player's hand with more cards in it than your hand."
    },
    "Nimble Gray" : {
        "Image" : '',
        "Class" : heroType.Warrior,
        "Effect" : cardEffect.NimbleGray,
        "Effect Roll" : 9,
        "Card Type"   : cardType.Hero,
        "Description" : "You may ATTACK any Monster card this turn even if you do not meet its Party requirement."
    },
    "Mimi" : {
        "Image" : '',
        "Class" : heroType.Wizard,
        "Effect" : cardEffect.Mimi,
        "Effect Roll" : 4,
        "Card Type"   : cardType.Hero,
        "Description" : "Choose a Hero card in any player's Party. Mimi's effect is that Hero card's effect (including roll cost) until the end of your turn. You may roll to use that effect immediately."
    },
    #Here to Sleigh
    #Banner Quest
}
#Banners
Banners = {
    "None" : {
        "Description" : "Temporary placeholder for src/active_player.py"
    }
}

#Main Deck, list of cards in the base game
mainDeck = [
    "Dodgy Dealer",
    "Fuzzy Cheeks",
    "Greedy Cheeks",
    "Lucky Bucky",
    "Mellow",
    "Napping Nibbles",
    "Peanut",
    "Tipsy Tootie",
    "Bad Axe",
    "Bear Claw",
    "Beary Wise",
    "Fury Knuckle",
    "Heavy Bear",
    "Pan Chucks",
    "Qi Bear",
    "Tough Teddy",
    "Calming Voice",
    "Guiding Light",
    "Holy Curselifter",
    "Iron Resolve",
    "Mighty Blade",
    "Radiant Horn",
    "Vibrant Glow",
    "Wise Shield",
    "Bullseye",
    "Hook",
    "Lookie Rookie",
    "Quick Draw",
    "Serious Grey",
    "Sharp Fox",
    "Wildshot",
    "Wily Red",
    "Kit Napper",
    "Meowzio",
    "Plundering Puma",
    "Shurkitty",
    "Silent Shadow",
    "Slippery Paws",
    "Sly Pickings",
    "Smooth Mimimeow",
    "Bun Bun",
    "Buttons",
    "Fluffy",
    "Hopper",
    "Snowball",
    "Spooky",
    "Whiskers",
    "Wiggles",
    "Bard Mask",
    "Decoy Doll",
    "Fighter Mask",
    "Guardian Mask",
    "Particularly Rust Coin",
    "Particularly Rust Coin",
    "Ranger Mask",
    "Really Big Ring",
    "Really Big Ring",
    "Thief Mask",
    "Wizard Mask",
    "Curse of the Snake's Eyes",
    "Curse of the Snake's Eyes",
    "Sealing Key",
    "Suspiciously Shiny Coin",
    "+1/-3 Modifier",
    "+1/-3 Modifier",
    "+1/-3 Modifier",
    "+1/-3 Modifier",
    "+2/-2 Modifier",
    "+2/-2 Modifier",
    "+2/-2 Modifier",
    "+2/-2 Modifier",
    "+2/-2 Modifier",
    "+2/-2 Modifier",
    "+2/-2 Modifier",
    "+2/-2 Modifier",
    "+2/-2 Modifier",
    "+3/-1 Modifier",
    "+3/-1 Modifier",
    "+3/-1 Modifier",
    "+3/-1 Modifier",
    "+4 Modifier",
    "+4 Modifier",
    "+4 Modifier",
    "+4 Modifier",
    "-4 Modifier",
    "-4 Modifier",
    "-4 Modifier",
    "-4 Modifier",
    "Call to the Fallen",
    "Critical Boost",
    "Critical Boost",
    "Destructive Spell",
    "Destructive Spell",
    "Enchanted Spell",
    "Enchanted Spell",
    "Entangling Trap",
    "Entangling Trap",
    "Forced Exchange",
    "Forceful Winds",
    "Winds of Change",
    "Winds of Change",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge",
    "Challenge"
    ]
dsDeck = [ #Dragon Sorcerer Expansion card list
    "Dragalter",
    "Distortivern",
    "Extraga",
    "Luut",
    "Mirroryu",
    "Oracon",
    "Renovern",
    "Shamanaga",
    "Smok",
    "Sorcerer Mask",
    "+6 DS Modifier",
    "-6 DS Modifier",
    "Egg of Fortune",
    "Sorcerer Challenge"
]
wadDeck = [ #Warriors and Druids Expansion card list
    "Big Buckley",
    "Buck Omens",
    "Doe Fallow",
    "Glowing Antler",
    "Maegisty",
    "Magus Moose",
    "Majestelk",
    "Stagguard",
    "Agile Dagger",
    "Blinding Blade",
    "Critical Fang",
    "Hardened Hunter",
    "Looting Lupo",
    "Silent Shield",
    "Tenacious Timber",
    "Wolfgang Pack",
    "Bottomless Bad",
    "Druid Mask",
    "Even Bigger Ring",
    "Temporal Hourglass",
    "Warrior Mask",
    "+1/-1 WaD Modifier",
    "+2/-1 WaD Modifier",
    "+4 WaD Modifier",
    "-4 WaD Modifier",
    "Cursed Glove",
    "Soul Tether",
    "Rapid Refresh",
    "Druid Challenge",
    "Warrior Challenge"
]
banDeck = [ #Berserkers and Necromancers Expansion card list
    "Bark Hexer",
    "Beholden Retriver",
    "Bone Collector",
    "Boston Terror",
    "Grim Pupper",
    "Hollow Husk",
    "Perfect Vessel",
    "Shadow Saint",
    "Annihilator",
    "Brawling Spirit",
    "Gruesome Gladiator",
    "Meowntain",
    "Rabid Beast",
    "Roaryal Guard",
    "Unbridled Fury",
    "Berserker Mask",
    "Biggest Ring Ever",
    "Goblet of Caffeination",
    "Necromancer Mask",
    "Silver Lining",
    "+2/-2 BaN Modifier",
    "+7 BaN Modifer",
    "Dragon's Bile",
    "Soulbound Grimoire",
    "Lightning Labrys",
    "Lightning Labrys",
    "Mass Sacrifice",
    "Mass Sacrifice",
    "Berserker Challenge",
    "Necromancer Challenge"
]
baqBanners = [ #Banner Quest Expansion list of banners
    "Bard Banner",
    "Berserker Banner",
    "Druid Banner",
    "Fighter Banner",
    "Guardian Banner",
    "Hunter's Trophy Banner",
    "Necromancer Banner",
    "Ranger Banner",
    "Thief Banner",
    "Warrior Banner",
    "Wizard Banner"
]
baqDeck = [ #Banner Quest Expansion card list
    "Bone Bruiser",
    "Crushing Crusader",
    "Deft Paw",
    "Grave Howl",
    "Loopy Lyricist",
    "Mystical Melody",
    "Shadow Striker",
    "Thorn Blade",
    "Ursine Protector",
    "Wild Hooves",
    "Prism Mask",
    "Prism Mask",
    "Prism Mask",
    "Chaos Mask",
    "Chaos Mask",
    "Morph Mask",
    "Morph Mask",
    "Morph Mask",
    "Relic Amp",
    "Relic Amp",
    "Synergy Boost",
    "Synergy Boost",
]
kseDeck = [ #Kickstarter Exclusive card list
    "Hamlet",
    "Bearserker",
    "Complex Illusion",
    "Enchantler",
    "Hoodwink",
    "Purring Bandit",
    "Nimble Gray",
    "Mimi",
    "Mysterious Feather",
    "Mask of Misfortune",
    "+1/-4 KSE Modifier",
    "+2/-3 KSE Modifier",
    "+3/-2 KSE Modifier",
    "+4/-1 KSE Modifier",
    "Captivating Spell",
    "Bard Challenge",
    "Fighter Challenge",
    "Guardian Challenge",
    "Ranger Challenge",
    "Thief Challenge",
    "Wizard Challenge"
]
limitedCardsDeck = [ #Cards from buying the vinyl figures
    "Howl of the Dead",
    "Reigning King"
]
htsDeck = [ #Here to Sleigh Expansion card list
    "Gift Bearer",
    "Santa Claws",
    "Christmas Carol",
    "Lil' Drummer  Bard",
    "Shiny Nose",
    "Snow Slinger",
    "Prancer",
    "Shooting Star",
    "Fireplace Fugitive",
    "Gift Bag Bandit",
    "Evergreen",
    "Holly Jolly",
    "Freshly Sharpened Skates",
    "Milk and Cookies",
    "Garbge Gift Challenge",
    "Garbge Gift Challenge",
    "Garbge Gift Challenge",
    "Good Gift Challenge",
    "Good Gift Challenge",
    "Good Gift Challenge",
]
htsGifts = [ #Gifts from Here to Sleigh
    "Bag of Holding Gifts",
    "EZ Mix Potions",
    "Mythical Mystery",
    "Rudolph's Nose",
    "Snows of Time",
    "The Gift of Destruction",
    "Warm Socks",
    "Endless Unwrapping",
    "Gag Gift",
    "Lump of Coal",
    "Mint Condition Mittens",
    "Potluck Surprise",
    "Really Itchy Sweater",
    "Watchful Medallion",
    "White Elephant",
]
monsterDeck = [ #Base Game list of Monsters
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
wadMonsterDeck = ["Feral Dragon","Muscipula Rex"]    #Monsters from Warriors and Druids
banMonsterDeck = ["Doom Bringer","Reptilian Ripper"] #Monsters from Berserkers and Necromancers
dsMonsterDeck = ["Calamity Mongrel"]                 #Monsters from Dragon Sorcerers
baqMonsterDeck = ["Chitin Scourge","Razor Tongue"]  #Monsters from Banner Quest
moeDeck = [ #Monster Expansion card list
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
    "Wicked Sea Serpent"
    ]
#Configs add cards to the deck in use
if not ranked:
    if WarriorsAndDruids:
        monsterDeck.append(wadMonsterDeck)
        mainDeck.append(wadDeck)
    if BerserkersAndNecromancers:
        monsterDeck.append(banMonsterDeck)
        mainDeck.append(banDeck)
    if DragonSorcerers:
        monsterDeck.append(dsMonsterDeck)
        mainDeck.append(dsDeck)
    if MonsterExpansion:
        monsterDeck.append(moeDeck)
    if HereToSleigh:
        mainDeck.append(htsDeck)
    if BannerQuest:
        monsterDeck.append(baqMonsterDeck)
        mainDeck.append(baqDeck)
p1Deck = [] #Player 1's deck in Ranked
p2Deck = [] #Player 2's deck in Ranked 
rankedMonsterDeck = [ #All unbanned Monsters in the Ranked deck
    "Abyss Queen",
    "Anuran Cauldron", #Considering Banning
    "Arctic Aries",
    "Bloodwing",
    "Corrupted Sabretooth",
    "Crowned Serpent",
    "Dark Dragon King",
    "Dracos",
    "Malamammoth",
    "Mega Slime", #Considering Banning
    "Orthus",
    "Rex Major",
    "Terratuga",
    "Titan Wyvern",
    "Warworn Owlbear",
    "Feral Dragon",
    "Muscipula Rex",
    "Doom Bringer", #Considering Banning
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
    #"Venemous Gemini",
    "Voltclaw Lion",
    "Wandering Behemoth",
    "Wicked Sea Serpent",
    "Chitin Scourge",
    "Razor Tongue",
    "Calamity Mongrel"
    ]
szlDeck = [] #ShadowzLmao's Ranked Deck