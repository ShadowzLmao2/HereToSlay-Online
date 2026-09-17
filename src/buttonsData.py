from draw import *
from main import *
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # Import PIL for PNG support

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
        "method": sys.exit,
        "centered": True,
    },
    "rankedButton": {
        "buttonName": "playButton",
        "x": 0,
        "y": 0,
        "type": "image",
        "value": 0, #The index of the image we want (I couldent get cardImageRef to work bc I'm dumb, if you can get it to work plz do)
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
