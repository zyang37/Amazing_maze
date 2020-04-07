def startMenu():

    import tkinter as tk
    from tkinter import Text
    import tkinter.font as tkFont
    import os

    root = tk.Tk()
    root.title("Amazing Maze")

    #the background image path
    background_image = tk.PhotoImage(file = "backgrounds/maze.png")

    canvas = tk.Canvas(root, height = 900, width = 900)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas.grid()

    fontStyle = tkFont.Font(family="Lucida Grande", size=40)
    gameLabel = tk.Label(root, bg = 'white', text="Amazing Maze", font = fontStyle)
    gameLabel.place(x = 250, y = 0)

    startButton = tk.Button(root, bg="white", bd = 3, text = "Start game", padx = 30, pady = 20)
    startButton.place(x = 250, y =750)

    loadButton = tk.Button(root, bg = 'white', bd = 3, text = "Load game", padx = 30, pady = 20)
    loadButton.place(x = 390, y = 750)

    difficultyButton = tk.Menubutton(root, bg = "white", bd = 3, text="Diffifulty", padx = 30, pady = 20)
    difficultyButton.place(x=530, y =750)

    difficultyButton.menu =  tk.Menu ( difficultyButton, tearoff = 0 )
    difficultyButton["menu"] =  difficultyButton.menu

    difficultyButton.menu.add_checkbutton (label="easy", variable=tk.IntVar())
    difficultyButton.menu.add_checkbutton (label="medium", variable=tk.IntVar())
    difficultyButton.menu.add_checkbutton (label="hard", variable=tk.IntVar())
    difficultyButton.menu.add_checkbutton (label="insane", variable=tk.IntVar())

    root.mainloop()

    return 

if __name__ == "__main__": 
    startMenu()