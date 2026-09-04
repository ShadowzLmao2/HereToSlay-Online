import os
from main import *
from data import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # Import PIL for PNG support
window = Tk()
window.geometry("1280x720")
window.title("Here to Slay Online")

defaultImgWidth = 140
defaultImgHeight = 200

#0 = main menu
#1 = game screen
currentScene = 0


def start() :
    
    #TODO: make these buttons do smth, all currently just quit the program
    #Declare all buttons in the opening screen
    #The layout is as follows:
    #buttonName = tk.Button(window, text='what button says', command=functionButtonExecutes, width=widthInLetters)
    img = resize_image('src/data/card_images/BaseGame/Cards/badAxe.png')
    playButton = tk.Button(window, text='Play', command=lambda: startGame(), width=40, height=2)
    rankedButton = tk.Button(window, text='Ranked', command=lambda: window.quit(), width=40, height=2)
    settingsButton = tk.Button(window, text='Settings', command=lambda: window.quit(), width=40, height=2)
    #quitButton = tk.Button(window, text='Quit', command=lambda: window.quit(), width=40, height=2)
    quitButton = tk.Button(window, image=img, command=lambda: window.quit(), width=img.width(), height=img.height())

    #Main Menu
    playButton.pack(ipadx=5, ipady=5, expand=True)
    #rankedButton.pack(ipadx=5, ipady=5, expand=True)
    settingsButton.pack(ipadx=5, ipady=5, expand=True)
    quitButton.pack(ipadx=5, ipady=5, expand=True)

    playButton.place(relx=.5,rely=.5,anchor="center")
    playButton.place(x=playButton.winfo_rootx(),y=playButton.winfo_y()-240)

    rankedButton.place(relx=.5,rely=.5,anchor="center")
    rankedButton.place(x=rankedButton.winfo_rootx(),y=rankedButton.winfo_y()-160)

    settingsButton.place(relx=.5,rely=.5,anchor="center")
    settingsButton.place(x=settingsButton.winfo_rootx(),y=settingsButton.winfo_y()-80)

    quitButton.place(relx=.5,rely=.5,anchor="center")
    quitButton.place(x=quitButton.winfo_rootx(),y=quitButton.winfo_y())

    window.mainloop()
    readFolder()

#resize image
def resize_image(path):
    """Load and resize an image using Pillow."""
    try:
        img = Image.open(path)  # Open image using pillow
        img = img.resize((defaultImgWidth, defaultImgHeight), Image.LANCZOS)  # High-quality resize
        return ImageTk.PhotoImage(img) #turn pillow img into tkinter img
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

#TODO: setup preloading all PhotoImage classes using this function to find each of their paths
def readFolder(): 
    # Replace 'path/to/your/folder' with the actual path
    folder_path = os.path.join('src/data/card_images/BaseGame', 'Cards')
    # Get all entries in the folder
    entries = os.listdir(folder_path)
    # Loop through entries and print their names
    for entry in entries:
        print(entry)