#from main import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("1920x1080")
window.title("Here to Slay Online")

#TODO: make these buttons do smth, all currently just quit the program
#Declare all buttons in the opening screen
#The layout is as follows:
#buttonName = tk.Button(window, text='what button says', command=functionButtonExecutes, width=widthInLetters)
playButton = tk.Button(window, text='Play', command=lambda: window.quit(), width=40, height=2)
rankedButton = tk.Button(window, text='Ranked', command=lambda: window.quit(), width=40, height=2)
settingsButton = tk.Button(window, text='Settings', command=lambda: window.quit(), width=40, height=2)
quitButton = tk.Button(window, text='Quit', command=lambda: window.quit(), width=40, height=2)

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