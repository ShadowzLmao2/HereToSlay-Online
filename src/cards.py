from enum import Enum
class cardEffect(Enum):
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

    #Action
    Challenge = 18
    Modifier = 19
    FuzzyCheeks = 20
    
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
        "Effect" : cardEffect.CharismaticSong,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Description" : "Each time you roll to use a Hero card's effect, +1 to your roll."
    },
    "Fist of Reason" : {
        "Class" : heroType.Fighter,
        "Effect" : cardEffect.FistOfReason,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Description" : "Each time you roll to CHALLENGE, +2 to your roll."
    },
    "Shadow Claw" : {
        "Class" : heroType.Thief,
        "Effect" : cardEffect.ShadowClaw,
        "Activatable" : True,
        "DLC" : originalGame.Base,
        "Description" : "Once per turn on your turn, you may spend an action point to pull a card from another player's hand."
    },
    "Cloaked Sage" : {
        "Class" : heroType.Wizard,
        "Effect" : cardEffect.CloakedSage,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Description" : "Each time you play a Magic card, DRAW a card."
    },
    "Divine Arrow" : {
        "Class" : heroType.Ranger,
        "Effect" : cardEffect.DivineArrow,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Description" : "Each time you roll to ATTACK a Monster card, +1 to your roll."
    },
    "Protecting Horn" : {
        "Class" : heroType.Guardian,
        "Effect" : cardEffect.ProtectingHorn,
        "Activatable" : False,
        "DLC" : originalGame.Base,
        "Description" : "Each time you play a Modifier card on a roll, +1 or -1 to that roll."
    },
    "Noble Shaman" : {
        "Class" : heroType.Druid,
        "Effect" : cardEffect.NobleShaman,
        "Activatable" : False,
        "DLC" : originalGame.WaD,
        "Description" : "Once per turn on each player's turn, you may choose any player's roll. -1 to that roll."
    },
    "Piercing Howl" : {
        "Class" : heroType.Warrior,
        "Effect" : cardEffect.PiercingHowl,
        "Activatable" : False,
        "DLC" : originalGame.WaD,
        "Description" : "Each time you roll, +1 to your roll for each Item card equipped to a Hero card in your party."
    },
    "Gnawing Dread" : {
        "Class" : heroType.Necromancer,
        "Effect" : cardEffect.GnawingDread,
        "Activatable" : True,
        "DLC" : originalGame.BaN,
        "Description" : "Once per turn on your turn, you may spend 2 action points to search the discard pile for a card and add it to your hand."
    },
    "Raging Manticore" : {
        "Class" : heroType.Berserker,
        "Effect" : cardEffect.RagingManticore,
        "Activatable" : False,
        "DLC" : originalGame.BaN,
        "Description" : "Each time you SLAY a Monster card, DRAW 2 cards."
    },
    "Fearless Flame" : {
        "Class" : heroType.Sorcerer,
        "Effect" : cardEffect.FearlessFlame,
        "Activatable" : False,
        "DLC" : originalGame.DrSo,
        "Description" : "Each time you roll the dice, you may DISCARD a card. If you do, +1 to your roll."
    },
    "Brutal Bow" : {
        "Class" : heroType.Fighter,
        "Secondary Class" : heroType.Ranger,
        "Effect" : cardEffect.BrutalBow,
        "Activatable" : False,
        "DLC" : originalGame.KSE,
        "Description" : "At the beginning of your turn, you may switch The Brutal Bow's class between Fighter and Ranger.\nEach time you DESTROY a Hero card, DRAW a card."
    },
    "Mystical Maestro" : {
        "Class" : heroType.Wizard,
        "Secondary Class" : heroType.Bard,
        "Effect" : cardEffect.MysticalMaestro,
        "Activatable" : False,
        "DLC" : originalGame.KSE,
        "Description" : "At the beginning of your turn, you may switch The Mystical Maestro's class between Mage and Bard.\nEach time you roll 4 or less (including Modifier cards), you may DRAW a card."
    },
    "Veiled Raider" : {
        "Class" : heroType.Guardian,
        "Secondary Class" : heroType.Thief,
        "Effect" : cardEffect.VeiledRaider,
        "Activatable" : False,
        "DLC" : originalGame.KSE,
        "Description" : "At the beginning of your turn, you may switch The Veiled Raider's class between Guardian and Thief.\nEach time you roll 12 or more (including Modifier cards), you may STEAL a Hero."
    },
    "Unstable Unicorn" : {
        "Class" : heroType.NoClass,
        "Effect" : cardEffect.UnstableUnicorn,
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
monsterDeck = [1,2,3,4,5]