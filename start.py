import pygame , random
from pygame.locals import *
from maze_gen import *
from helper import *
from Startmenu import *

# helper functions
def find_random_spot(listmaze):
    s = []
    for i in range(len(listmaze)):
        for j in range(len(listmaze[0])):
            if listmaze[i][j] == 1:
                s.append([j,i])
    random.shuffle(s)
    return s[0]

def draw_maze(screen):
   for row in range(len(maze)):
       for column in range(len(maze[0])):
           screen.fill(cell_colors[maze[column][row]], get_cell_rect((row, column), screen))
           if (maze[row][column] == 'x'):
               score_value += 10

def get_cell_rect(coordinates, screen):
   row, column = coordinates
   cell_width = screen.get_width() / len(maze)
   adjusted_width = cell_width - cell_margin
   return pygame.Rect(row * cell_width + cell_margin / 2, column * cell_width + cell_margin / 2, adjusted_width, adjusted_width)

def draw_player(playerImg, screen):
   rect = playerImg.get_rect()
   rect.center = get_cell_rect(current_position, screen).center
   screen.blit(playerImg, rect)

def draw_star(star,screen,position):
    rect = star.get_rect()
    rect.center = get_cell_rect(position,screen).center
    screen.blit(star,rect)

def drawScore(score, screen):
    scoreSurf = BASICFONT.render('score: %s'%(score),True,(0,0,0))
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (700,5)
    screen.blit(scoreSurf,scoreRect)

def move(dx, dy):
    x, y = current_position
    nx, ny = x + dx, y + dy
    if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[ny][nx]:
       current_position[0] = nx
       current_position[1] = ny

def move_enemy():
    tmp = Arandom_move()
    x = enemy_position[0]
    y = enemy_position[1]
    nx, ny = x + tmp[0], y + tmp[1]
    if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[ny][nx]:
       enemy_position[0] = nx
       enemy_position[1] = ny

# ========================================== main ==========================================
'''
maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''
# maze infor
maze = maze_gen(17, 17)
resolution = (800, 800)
cell_margin = 0.5
cell_colors = (255, 255, 255), (255, 192, 203)

# starting point
current_position = [0, 1]
enemy_position = find_random_spot(maze)

# set objects size
object_size = (20, 20)

#icon
icon = pygame.image.load('img/icon.png')
star = pygame.image.load('img/star.png')
enemy = pygame.image.load('img/enemy.png')
playerImg = pygame.image.load('img/mushroom.png')

playerImg = pygame.transform.scale(playerImg, object_size)
star = pygame.transform.scale(star,object_size)
enemy = pygame.transform.scale(enemy,object_size)

pygame.display.set_icon(icon)
#score
score = 0

def main():
    global score, BASICFONT, FPSCLOCK, maze
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode(resolution)
    screen.fill(cell_colors[1])
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption("Amazing Maze")
    star_store = (find_random_spot(maze))
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
        if current_position==star_store:
            star_store = (find_random_spot(maze))
            delete_random_wall(maze)
            score+=1

        draw_maze(screen)
        draw_player(playerImg, screen)
        draw_star(star,screen,star_store)
        # test
        move_enemy()
        draw_star(enemy,screen,enemy_position)
        drawScore(score,screen)
        pygame.display.update()
        FPSCLOCK.tick(30)



if __name__ == "__main__":
    gameStat = []
    gameStat = startMenu()
   
    if(gameStat[0][0]):
        main()
    
    pygame.quit()
