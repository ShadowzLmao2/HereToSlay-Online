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
    
class cardType(Enum):
    NoCard  = 0
    Action  = 1
    Magic   = 2
    Item    = 3
    Hero    = 4
    Leader  = 5
    Monster = 6
    Any     = 7

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
    KSE = 7

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
    }
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