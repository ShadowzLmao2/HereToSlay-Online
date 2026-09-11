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

cardTotal = 0

#0 = main menu
#1 = game screen
currentScene = 0

buttons = []
#array that is synced up with one above, where every button's current image (if applicable) is stored using the same index as the button
currentImage = []

pngCount = 0

#Stores the positions of buttons NOT on screen
buttonPositions = []

#cardnames
leaderNames = []
monsterNames = []
cardNames = []

firstImage = 0

cardImages = []

def start() :

    #imageNames = readFolder('src', 'card_images')
    #imagePaths = setupImages(imageNames)
    #TODO: make these buttons do smth, all currently just quit the program
    #Declare all buttons in the opening screen
    #The layout is as follows:
    #buttonName = tk.Button(window, text='what button says', command=functionButtonExecutes, width=widthInLetters)
    
    leaderNames = populateLeaderNames()
    monsterNames = populateMonsterNames()
    cardNames = populateCardNames()
    cardImages = populateCardImages(cardNames)
    print(str(cardTotal) + " cards in total(262 expected)")
    for card in cardImages:
        if card != None:
            firstImage = cardImages.index(card)

    buttons.append(tk.Button(window, text='Play', command=lambda: startGame(), width=40, height=2, name='playButton'))
    buttons.append(tk.Button(window, text='Ranked', command=lambda: window.quit(), width=40, height=2, name='rankedButton'))
    buttons.append(tk.Button(window, text='Settings', command=lambda: window.quit(), width=40, height=2, name='settingsButton'))
    buttons.append(tk.Button(window, image=cardImages[len(cardImages) - 1], command=lambda: window.quit(), width=cardImages[len(cardImages) - 1].width(), height=cardImages[len(cardImages) - 1].height(), name='quitButton'))
    #buttons.append(tk.Button(window, text='Quit', command=lambda: window.quit(), width=40, height=2, name='buttons[3]))

    print(str(buttons[3].cget('image')).removeprefix('pyimage'))

    buttons.append(tk.Button(window, text='test', command=lambda: window.quit(), width=40, height=2, name='b4'))
    print(buttons[4])

    name = "Charismatic Song"
    print(getImagePath(Leaders, name))
    #buttons[3].config(image=cardImages[0], bd=0, relief='flat', highlightthickness=0)

    #Main Menu
    buttons[0].pack(ipadx=5, ipady=5, expand=True)
    #buttons[1].pack(ipadx=5, ipady=5, expand=True)
    buttons[2].pack(ipadx=5, ipady=5, expand=True)
    buttons[3].pack(ipadx=5, ipady=5, expand=True)

    buttons[0].place(relx=.5,rely=.5,anchor="center")
    buttons[0].place(x=buttons[0].winfo_rootx(),y=buttons[0].winfo_y()-240)

    buttons[1].place(relx=.5,rely=.5,anchor="center")
    buttons[1].place(x=buttons[1].winfo_rootx(),y=buttons[1].winfo_y()-160)

    buttons[2].place(relx=.5,rely=.5,anchor="center")
    buttons[2].place(x=buttons[2].winfo_rootx(),y=buttons[2].winfo_y()-80)

    buttons[3].place(relx=.5,rely=.5,anchor="center")
    buttons[3].place(x=buttons[3].winfo_rootx(),y=buttons[3].winfo_y())

    #Causes the button to hide itself
    #I believe it looses its x and y values, so TODO: store button x and y vals seperately
    #Note: if you use place, place_forget, if you use pack, pack_forget, etc
    #buttons[3].place_forget()
    hide(buttons[2])

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
def getImagePath(dict, card):
    sub = dict[card]
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

#Switch screens
#store positions of buttons currently on screen
'''def screenSwitch(screen):
    match screen:
        case 0:
            '''

def populateLeaderNames():
    global cardTotal
    out = []
    num = 0
    for name in Leaders:
        out.append(name)
        num += 1
        cardTotal += 1
    print(str(num) + " leader cards (19 expected)")
    return out

def populateMonsterNames():
    global cardTotal
    out = []
    num = 0
    for name in Monsters:
        out.append(name)
        num += 1
        cardTotal += 1
    print(str(num) + " monster cards (36 expected)")
    return out

def populateCardNames():
    global cardTotal
    out = []
    num = 0
    for name in Cards:
        out.append(name)
        num += 1
        cardTotal += 1
    print(str(num) + " cards (207 expected)")
    return out

def populateCardImages(names):
    out = []
    for name in names:
        out.append(resize_image(getImagePath(Cards, name))) 
    out = [x for x in out if x is not None]
    return out