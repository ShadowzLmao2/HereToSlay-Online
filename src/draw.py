import os
import sys
from buttons import *
from cards import *
from main import *
from card_images import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # Import PIL for PNG support
from buttonsData import *
window = Tk()
window.geometry("1280x720")
window.title("Here to Slay Online")

defaultImgWidth = 140
defaultImgHeight = 200

yCenter = 720/2
xCenter = 1280/2

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

leaderImages = []
monsterImages = []
cardImages = []

#offset of arrays of images, as pyimage #s are decided in order of declaration
leadersSize = 19
monstersSize = 36
cardsSize = 1

def start() :

    #imageNames = readFolder('src', 'card_images')
    #imagePaths = setupImages(imageNames)
    #TODO: make these buttons do smth, all currently just quit the program
    #Declare all buttons in the opening screen
    #The layout is as follows:
    #buttonName = tk.Button(window, text='what button says', command=functionButtonExecutes, width=widthInLetters)

    window.bind("<Configure>", on_resize)
    
    leaderNames = populateLeaderNames()
    leaderImages = populateLeaderImages(leaderNames)
    print("leader start" + str(leaderImages[0]))
    monsterNames = populateMonsterNames()
    monsterImages = populateMonsterImages(monsterNames)
    print("monster start" + str(monsterImages[0]))
    cardNames = populateCardNames()
    cardImages = populateCardImages(cardNames)
    print("card start" + str(cardImages[0]))
    print(str(cardTotal) + " cards in total(262 expected)")
    for card in cardImages:
        if card != None:
            firstImage = cardImages.index(card)

    compareCards(Leaders, Monsters, Cards)

    #Create a frame to hold the scrollbar
    mainFrame = Frame(window)
    mainFrame.pack(fill=BOTH, expand=1)

    #Canvas is put into frame, this is what scrolls when the scrollbar is interacted with
    canvas = Canvas(mainFrame)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #create the scrollbar
    scrollbar = ttk.Scrollbar(mainFrame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    #Configure the scrollbar to scroll the canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #Create secondary frame inside canvas
    secondFrame = Frame(canvas)

    #Add second frame to a new window in canvas
    canvas.create_window((0,0), window=secondFrame, anchor="nw")

    #Because a button cannot have an attribute added after it is declared, declare both an img and a text and have them both blank, then call buttonSetup to assign
    buttons.append(tk.Button(secondFrame, text='', image=None, command=doNothing, width=40, height=2, name='playButton'))
    #test(buttons[0])
    buttons.append(tk.Button(secondFrame, text='', image=None, command=lambda: compareCards(Leaders, Monsters, Cards), width=40, height=2, name='rankedButton'))
    setupButton(buttons[1], removeStart(buttons[1]))
    buttons.append(tk.Button(secondFrame, text='', image=None, command=lambda: window.quit(), width=40, height=2, name='settingsButton'))
    setupButton(buttons[2], removeStart(buttons[2]))
    #buttons.append(tk.Button(secondFrame, image=cardImages[len(cardImages) - 1], command=lambda: window.quit(), width=cardImages[len(cardImages) - 1].width(), height=cardImages[len(cardImages) - 1].height(), name='quitButton'))
    buttons.append(tk.Button(secondFrame, text='', image=None, command=lambda: window.quit(), width=40, height=2, name='quitButton'))
    setupButton(buttons[3], removeStart(buttons[3]))

    #print(str(buttons[3].cget('image')).removeprefix('pyimage'))
    #print(cardImages[int(str(buttons[3].cget('image')).removeprefix('pyimage')) - cardsSize])
    print(cardImages[70])
    print(cardImages[71])

    buttons.append(tk.Button(window, text='test', command=lambda: window.quit(), width=40, height=2, name='b4'))
    print(buttons[4])

    name = "Charismatic Song"
    print(getImagePath(Leaders, name))
    #buttons[3].config(image=cardImages[0], bd=0, relief='flat', highlightthickness=0)

    #Main Menu
    #buttons[0].pack(ipadx=5, ipady=5, expand=True)
    #buttons[1].pack(ipadx=5, ipady=5, expand=True)
    #buttons[2].pack(ipadx=5, ipady=5, expand=True)
    #buttons[3].pack(ipadx=5, ipady=5, expand=True)

    setupButton(buttons[0], removeStart(buttons[0]))

    #Unless this runs, the window width is not updated
    window.update_idletasks()

    #secondFrame.grid_columnconfigure(0, weight=1)

    buttons[0].grid(row=1, column=1,ipadx=5, ipady=5, padx=xCenter-160)
    buttons[1].grid(row=3, column=1,ipadx=5, ipady=5)
    buttons[2].grid(row=5, column=1,ipadx=5, ipady=5)
    buttons[3].grid(row=7, column=1,ipadx=5, ipady=5)

    #Causes the button to hide itself
    #I believe it looses its x and y values, so TODO: store button x and y vals seperately
    #Note: if you use place, place_forget, if you use pack, pack_forget, etc
    #buttons[3].place_forget()
    #hide(buttons[2])

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
        return 'src/card_images/default.png'
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
    global cardsSize
    cardsSize += len(out)
    return out

def populateLeaderImages(names):
    out = []
    for name in names:
        out.append(resize_image(getImagePath(Leaders, name))) 
    out = [x for x in out if x is not None]
    return out

def populateMonsterImages(names):
    out = []
    for name in names:
        out.append(resize_image(getImagePath(Monsters, name))) 
    out = [x for x in out if x is not None]
    global monstersSize
    monstersSize += len(out)
    monstersSize += (cardsSize - 1)
    return out

def compareCards(leaders, monsters, cards):
    cardsMissing = 0

    for entry in leaderNames:
        if valueInDict(mainDeck, entry) != True:
            continue
        elif valueInDict(dsDeck, entry) != True:
            continue
        elif valueInDict(wadDeck, entry) != True:
            continue
        elif valueInDict(banDeck, entry) != True:
            continue
        elif valueInDict(baqBanners, entry) != True:
            continue
        elif valueInDict(baqDeck, entry) != True:
            continue
        elif valueInDict(kseDeck, entry) != True:
            continue
        elif valueInDict(limitedCardsDeck, entry) != True:
            continue
        elif valueInDict(htsDeck, entry) != True:
            continue
        elif valueInDict(htsGifts, entry) != True:
            continue
        elif valueInDict(monsterDeck, entry) != True:
            continue
        else:
            print(entry + " is missing from the list")
            cardsMissing += 1
    for entry in monsterNames:
        if valueInDict(mainDeck, entry) != True:
            continue
        elif valueInDict(dsDeck, entry) != True:
            continue
        elif valueInDict(wadDeck, entry) != True:
            continue
        elif valueInDict(banDeck, entry) != True:
            continue
        elif valueInDict(baqBanners, entry) != True:
            continue
        elif valueInDict(baqDeck, entry) != True:
            continue
        elif valueInDict(kseDeck, entry) != True:
            continue
        elif valueInDict(limitedCardsDeck, entry) != True:
            continue
        elif valueInDict(htsDeck, entry) != True:
            continue
        elif valueInDict(htsGifts, entry) != True:
            continue
        elif valueInDict(monsterDeck, entry) != True:
            continue
        else:
            print(entry + " is missing from the list")
            cardsMissing += 1

    for entry in cardNames:
        if valueInDict(mainDeck, entry) != True:
            continue
        elif valueInDict(dsDeck, entry) != True:
            continue
        elif valueInDict(wadDeck, entry) != True:
            continue
        elif valueInDict(banDeck, entry) != True:
            continue
        elif valueInDict(baqBanners, entry) != True:
            continue
        elif valueInDict(baqDeck, entry) != True:
            continue
        elif valueInDict(kseDeck, entry) != True:
            continue
        elif valueInDict(limitedCardsDeck, entry) != True:
            continue
        elif valueInDict(htsDeck, entry) != True:
            continue
        elif valueInDict(htsGifts, entry) != True:
            continue
        elif valueInDict(monsterDeck, entry) != True:
            continue
        else:
            print(entry + " is missing from the list")
            cardsMissing += 1
    print("doneChecking")
    print(str(cardsMissing) + " cards missing")


def valueInDict(input, value):
    for entry in input:
        if input == value:
            return True
        else:
            continue
    return False



def on_resize(event):
    global yCenter
    global xCenter
    # CRITICAL: Check if the event was triggered by the root window itself, 
    # and not by one of its child widgets.
    if event.widget == window:
        print(f"Window resized! New width: {event.width}, New height: {event.height}")
        yCenter = event.height/2
        xCenter = event.width/2

def isCentered(dict):
    if dict["centered"]:
        return True
    else:
        return False

#Search StaticButtons dict for button name, and find the type, then assign the text or image
def setupButton(button, whatButton):
    global StaticButtons
    global cardImages
    global leaderImages
    global cardNames
    if len(leaderImages) == 0:
        leaderNames = populateLeaderNames()
        leaderImages = populateLeaderImages(leaderNames)
    buttonType = ""
    #Loop until the name is found.
    for key, value in StaticButtons.items():
        #Debugging
        print("Started Checking StaticButtons")
        #Check what value
        print("Value is "  + str(value))
        if str(key) == whatButton:
            button.config(command=value["method"])
            if value["type"] == "image":
                print("This is an image button")
                button.config(image=leaderImages[value["value"]], width=(leaderImages[value["value"]].width()), height=leaderImages[value["value"]].height())
                print(value["value"])
            elif value["type"] == "text":
                print("This is a text button")
                button.config(text = value["value"])

def test(button):
    button.config(text='test')

#Concat string starting from left until the last known value of the stop
def removeUntilVal(value, stop):
    out = value[(value.rfind(stop) + 1):]
    print("final is " + out)
    return out
#The full name of a button in tkinter is all of the frames and windows, then the button name, so this isolates and returns the button name
def removeStart(button):
    name = str(button)
    return removeUntilVal(name, '.')

def quitWindow():
    sys.exit()