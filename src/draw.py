import os
from buttons import *
from cards import *
from main import *
from card_images import *
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

pngCount = 0

#Stores the positions of buttons NOT on screen
buttonPositions = []


def start() :

    #imageNames = readFolder('src', 'card_images')
    #imagePaths = setupImages(imageNames)
    #TODO: make these buttons do smth, all currently just quit the program
    #Declare all buttons in the opening screen
    #The layout is as follows:
    #buttonName = tk.Button(window, text='what button says', command=functionButtonExecutes, width=widthInLetters)
    img = resize_image('src/card_images/BaseGame/Cards/badAxe.png')
    playButton = tk.Button(window, text='Play', command=lambda: startGame(), width=40, height=2)
    rankedButton = tk.Button(window, text='Ranked', command=lambda: window.quit(), width=40, height=2)
    settingsButton = tk.Button(window, text='Settings', command=lambda: window.quit(), width=40, height=2)
    #quitButton = tk.Button(window, text='Quit', command=lambda: window.quit(), width=40, height=2)
    quitButton = tk.Button(window, image=img, command=lambda: window.quit(), width=img.width(), height=img.height())

    name = "Charismatic Song"
    print(getLeaderImagePath(name))

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

    #Causes the button to hide itself
    #I believe it looses its x and y values, so TODO: store button x and y vals seperately
    #Note: if you use place, place_forget, if you use pack, pack_forget, etc
    #rankedButton.place_forget()
    hide(rankedButton)

    window.mainloop()

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

'''def readFolder(path, folderName): #read all the files in a folder
    contents = []
    out = []
    # Replace 'path/to/your/folder' with the actual path
    folder_path = os.path.join(path, folderName)
    # Get all entries in the folder
    entries = os.listdir(folder_path)
    # Loop through entries and print their names
    for entry in entries:
        contents.append(entry.strip())
        print(entry)
        #get rid of all values that arent a png
    out = keepOnlyPNG(contents, path, folderName)
    return out

def keepOnlyPNG(list, currentPath, currentFolder): 
    out = []
    global pngCount
    for item in list:
        if(item[-4:] == '.png'): #if the file is a png add it to the list
            out.append(currentPath + '/' + item)
            pngCount += 1 #test variable
        else:
            #if the value isnt a png, it must be a folder, so get all images from that as well
            out.extend(readFolder((currentPath + '/' + currentFolder),item))
    return out

def setupImages(paths):
    images = []
    for path in paths:
        images.append(resize_image(path))
    return images'''

#DO NOT DELETE, it doesnt work outside of a function
def getLeaderImagePath(leader):
    sub = Leaders[leader]
    return sub.get("Image")

#hide button
def hide(button):
    button.place_forget()
    button.grid_forget()
    button.pack_forget()



#get the button's position, return as a position object
def getPos(button):
    out = position(button.winfo_rootx(), button.winfo_rooty())
    return out


#button possition class so when the list is checked the button name will be stored to avoid duplicates
#pass in position object, as well as a button object, position is stored, button has its text stored
class buttonPos:
    pos = position(0,0)
    buttonTxt = ""
    def __init__(self, pos, button):
        self.pos = pos
        buttonTxt = button['text']
#Switch to