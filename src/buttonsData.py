from draw import *
from main import *

#Dictionary containing all of the button data for buttons that are not intended to move
StaticButtons = {
    #"ButtonName": {
    #    "buttonName": "playButton",
    #    "x": 0,
    #    "y": 0,
    #    "type": "text",
    #    "value": 
    #    "centered": True,
    #    "reference": window.quit()
    #},
    'playButton': {
        "buttonName": 'playButton',
        "x": 0,
        "y": 0,
        "type": 'text',
        "value": 'Start',
        "method": startGame,
        "centered": True,
    },
    "rankedButton": {
        "buttonName": "playButton",
        "x": 0,
        "y": 0,
        "type": "text",
        "value": "Ranked",
        "method": startGame,
        "centered": True,
    },
    "settingsButton": {
        "buttonName": "playButton",
        "x": 0,
        "y": 0,
        "type": "text",
        "value": "Settings",
        "method": startGame,
        "centered": True,
    },
    "quitButton": {
        "buttonName": "playButton",
        "x": 0,
        "y": 0,
        "type": "text",
        "value": "Quit",
        "method": startGame,
        "centered": True,
    },
}

