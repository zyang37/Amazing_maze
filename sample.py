# Create a simple maze by drawing a grid of squares defined in a 2D list of
# booleans and an ASCII character to represent the player.  The player can move
# along squares marked "1".
#
# Run with the following command:
#   python pygame-ascii-maze.py

import pygame
from pygame.locals import *
import tkinter as tk
import tkinter.font as tkFont

grid = [[0, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [0, 1, 0, 1, 1],
       [0, 1, 0, 1, 0],
       [0, 1, 1, 1, 0]]
resolution = (750, 750)
cell_margin = 14
cell_colors = (255, 255, 255), (255, 192, 203)
player_character = "rus"
player_color = (255, 255, 255)
player_size = 60
current_position = [0, 1]
start = False

def main():
   pygame.init()
   screen = pygame.display.set_mode(resolution)
   screen.fill(cell_colors[1])
   player = pygame.font.Font(None, player_size).render(player_character,
                                                       False, player_color)
   while True:
       for event in pygame.event.get():
           if event.type == KEYDOWN:
               key = event.key
               if key == K_UP:
                   move(0, -1)
               elif key == K_RIGHT:
                   move(1, 0)
               elif key == K_DOWN:
                   move(0, 1)
               elif key == K_LEFT:
                   move(-1, 0)
           elif event.type == QUIT:
               return
       draw_maze(screen)
       draw_player(player, screen)
       pygame.display.update()

def draw_maze(screen):
   for row in range(len(grid)):
       for column in range(len(grid[0])):
           screen.fill(cell_colors[grid[column][row]],
                       get_cell_rect((row, column), screen))

def get_cell_rect(coordinates, screen):
   row, column = coordinates
   cell_width = screen.get_width() / len(grid)
   adjusted_width = cell_width - cell_margin
   return pygame.Rect(row * cell_width + cell_margin / 2,
                      column * cell_width + cell_margin / 2,
                      adjusted_width, adjusted_width)

def draw_player(player, screen):
   rect = player.get_rect()
   rect.center = get_cell_rect(current_position, screen).center
   screen.blit(player, rect)

def move(dx, dy):
   x, y = current_position
   nx, ny = x + dx, y + dy
   if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and \
      grid[ny][nx]:
       current_position[0] = nx
       current_position[1] = ny

def startGame():
    global start
    start = True

def menu():
    root = tk.Tk()
    root.title("Amazing Maze")

    #the background image path
    background_image = tk.PhotoImage(file = "src/pic2.png")

    canvas = tk.Canvas(root, height = 900, width = 900)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas.grid()

    fontStyle = tkFont.Font(family="Lucida Grande", size=40)
    gameLabel = tk.Label(root, bg = 'white', text="Amazing Maze", font = fontStyle)
    gameLabel.place(x = 250, y = 0)

    startButton = tk.Button(root, bg="white", bd = 3, text = "Start game", command = lambda:[startGame(), root.destroy()], padx = 30, pady = 20)
    startButton.place(x = 300, y =700)

    loadButton = tk.Button(root, bg = 'white', bd = 3, text = "Load game", padx = 30, pady = 20)
    loadButton.place(x = 440, y = 700)

    difficultyButton = tk.Menubutton(root, bg = "white", bd = 3, text="Diffifulty", padx = 30, pady = 20)
    difficultyButton.place(x=580, y =700)

    difficultyButton.menu =  tk.Menu ( difficultyButton, tearoff = 0 )
    difficultyButton["menu"] =  difficultyButton.menu

    difficultyButton.menu.add_checkbutton ( label="easy", variable=tk.IntVar() )
    difficultyButton.menu.add_checkbutton ( label="medium", variable=tk.IntVar() )
    difficultyButton.menu.add_checkbutton ( label="hard", variable=tk.IntVar() )

    root.mainloop()
    
    return 

if __name__ == "__main__":
    
    level = menu()

    print(level)
    if start == True:
        main()
    
    pygame.quit()
