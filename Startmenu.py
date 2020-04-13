import tkinter as tk
from tkinter import *
#from tkinter import Text
import tkinter.font as tkFont
#from PIL import Image, ImageTk
import os

def start(gameStat):
    gameStat[0] = 1

def startMenu():

    gameStat = [0]

    root = tk.Tk()
    root.title("Amazing Maze")

    canvas = tk.Canvas(root, height = 850, width = 850)
    canvas.pack(fill=tk.BOTH, expand=tk.YES)

    background_image = tk.PhotoImage(file = "backgrounds/maze.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    icon = tk.PhotoImage(file = "img/icon.png")
    root.iconphoto(False, icon)

    canvas.grid()

    fontStyle = tkFont.Font(family="Lucida Grande", size=60)
    gameLabel = tk.Label(root, bg = 'white', text="Amazing Maze", font = fontStyle)
    gameLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

    startButton = tk.Button(root, bg="white", bd = 3, text = "Start game", command = lambda:[start(gameStat), root.destroy()], padx = 50, pady = 30)
    startButton.place(relx=0.25, rely=0.89, anchor=CENTER)

    loadButton = tk.Button(root, bg = 'white', bd = 3, text = "Load game", padx = 50, pady = 30)
    loadButton.place(relx=0.5, rely=0.89, anchor=CENTER)

    # Create a Tkinter variable
    tkvar = StringVar(root)
    tkvar.set('medium') # set the default option
    popupMenu = OptionMenu(canvas, tkvar, 'easy','medium','hard','insane')
    popupMenu.config(width=15)
    popupMenu.place(relx=0.75, rely=0.88, anchor=CENTER)

    canvas.configure(background='#90EE90')
    gameLabel.config(bg='#90EE90')
    # on change dropdown value
    def change_dropdown(*args):
        print(tkvar.get())
        if tkvar.get()=='easy':
            canvas.configure(background='#FFB6C1')
            gameLabel.config(bg='#FFB6C1')
        elif tkvar.get()=='medium':
            canvas.configure(background='#90EE90')
            gameLabel.config(bg='#90EE90')
        elif tkvar.get()=='hard':
            canvas.configure(background='#00BFFF')
            gameLabel.config(bg='#00BFFF')
        elif tkvar.get()=='insane':
            canvas.configure(background='#F08080')
            gameLabel.config(bg='#F08080')

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)

    '''
    difficultyButton = tk.Menubutton(root, bg = "white", bd = 3, text="Diffifulty", padx = 50, pady = 30)
    difficultyButton.place(relx=0.75, rely=0.89, anchor=CENTER)
    difficultyButton.menu =  tk.Menu ( difficultyButton, tearoff = 0 )
    difficultyButton["menu"] =  difficultyButton.menu
    difficultyButton.menu.add_checkbutton (label="easy", variable=tk.IntVar())
    difficultyButton.menu.add_checkbutton (label="medium", variable=tk.IntVar())
    difficultyButton.menu.add_checkbutton (label="hard", variable=tk.IntVar())
    difficultyButton.menu.add_checkbutton (label="insane", variable=tk.IntVar())
    '''

    root.mainloop()
    return gameStat, tkvar.get()

'''
if __name__ == "__main__":
    stat, level = startMenu()
    print(stat)
    print(level)
'''
