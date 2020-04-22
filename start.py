import pygame , random
from pygame.locals import *
from maze_gen import *
from helper import *
from Startmenu import startMenu
import time
import sys

# helper functions
def find_random_spot(listmaze):
    s = []
    for i in range(len(listmaze)):
        for j in range(len(listmaze[0])):
            if listmaze[i][j] == 1:
                s.append([j,i])
    random.shuffle(s)
    return s[0]

def find_spot_center(listmaze):
    s = []
    for i in range(len(listmaze)):
        for j in range(len(listmaze[0])):
            if listmaze[i][j] == 1:
                s.append([j,i])
    while distance(s[0], [0,1])<6 or distance(s[0], [len(listmaze)-1,len(listmaze[0])-2])<6:
        random.shuffle(s)

    return s[0]

def draw_maze(screen):
   for row in range(len(maze)):
       for column in range(len(maze[0])):
           screen.fill(cell_colors[maze[column][row]], get_cell_rect((row, column), screen))
           # if (maze[row][column] == 'x'):
           #     score_value += 10

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

def move_enemy(enemy_position):
    tmp = Arandom_move()
    x = enemy_position[0]
    y = enemy_position[1]
    nx, ny = x + tmp[0], y + tmp[1]
    if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]) and maze[ny][nx]:
       enemy_position[0] = nx
       enemy_position[1] = ny
    return enemy_position

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

def main(level, enemies):
    global score, BASICFONT, FPSCLOCK, maze, resolution

    pygame.init()

    icon = pygame.image.load('img/icon.png')
    star = pygame.image.load('img/shovel.png')
    enemy = pygame.image.load('img/enemy.png')
    playerImg = pygame.image.load('img/mushroom.png')
    exitlogo = pygame.image.load('img/exit.png')
    hint = pygame.image.load('img/hint.png')
    playerImg = pygame.transform.scale(playerImg, object_size)
    star = pygame.transform.scale(star,object_size)
    enemy = pygame.transform.scale(enemy,object_size)
    exitlogo = pygame.transform.scale(exitlogo,object_size)
    hint = pygame.transform.scale(hint, object_size)
    pygame.display.set_icon(icon)

    #print("1: {}".format(pygame.display.get_init()))
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode(resolution)
    #print("2: {}".format(pygame.display.get_init()))
    screen.fill(cell_colors[1])
    #print("3: {}".format(pygame.display.get_init()))
    #BASICFONT = pygame.font.SysFont("comicsansms", 18)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    #print("4: {}".format(pygame.display.get_init()))
    pygame.display.set_caption("Amazing Maze")
    #star_store = find_random_spot(maze)
    #hint_store = find_random_spot(maze)
    star_store = find_spot_center(maze)
    hint_store = find_spot_center(maze)

    hintTimer = False
    enemyTimer = True

    exit_location = [len(maze)-1,len(maze[0])-2]
    #print(len(maze), len(maze[0]))
    #print(exit_location)
    over = 0
    win = 0

    #print("start loop")
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and (win or over):
                print("key press!")
                #time.sleep(1)
                pygame.quit()
                return
            elif event.type == KEYDOWN:
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
                save_game(maze, level, current_position)
                print("maze saved")
                pygame.quit()
                sys.exit()
                #return

        # star
        if current_position==star_store:
            star_store = find_spot_center(maze)
            #delete_random_wall(maze)
            delete_random_surround_wall(maze, current_position)
            score+=1

        # when the player get hint position, show the right path for 5 seconds
        if current_position==hint_store:
            hint_store = find_spot_center(maze)
            show_path(maze, current_position[1], current_position[0])
            start_ticks = pygame.time.get_ticks()
            hintTimer = True

        # timer start
        if (hintTimer == True):
            hintSeconds = (pygame.time.get_ticks()-start_ticks)/1000
            if (hintSeconds > 5):
                clear_path(maze)
                hintTimer = False

        # maze
        draw_maze(screen)

        # player
        draw_player(playerImg, screen)

        # star
        draw_star(star,screen,star_store)

        # score
        drawScore(score,screen)

        # hint
        draw_star(hint, screen, hint_store)

        # exit
        draw_star(exitlogo, screen, exit_location)

        # enemies move
        if (enemyTimer == True):
            enemy_start_ticks = pygame.time.get_ticks()
            enemyTimer = False

        if ((pygame.time.get_ticks()-enemy_start_ticks)/1000 > 0.2):
            enemyTimer = True
            for e in enemies:
                enemy_position = e
                enemy_position = move_enemy(enemy_position)

        # display enemies
        for e in enemies:
            draw_star(enemy,screen,e)

        if current_position in enemies:
            if not over:
                print("GAME OVER\n")
            over = 1

        if current_position == exit_location:
            if not win:
                print("WIN\n")
            win = 1

        # gameover or win
        if over:
            fontB = pygame.font.SysFont("comicsansms", 150)
            fontS = pygame.font.SysFont("comicsansms", 45)
            GAMEOVER = fontB.render("GAME OVER!!!", True, (255,127,80))
            ANYKEYS = fontS.render("Press any key to quit", True, (0, 128, 0))
            screen.blit(GAMEOVER,(resolution[0]/2 - GAMEOVER.get_width() // 2, resolution[0]/2.5 - GAMEOVER.get_height() // 2))
            screen.blit(ANYKEYS,(resolution[0]/2 - ANYKEYS.get_width() // 2, resolution[0]/2 - ANYKEYS.get_height() // 2))
        elif win:
            fontB = pygame.font.SysFont("comicsansms", 150)
            fontS = pygame.font.SysFont("comicsansms", 45)
            WIN = fontB.render("GOOD JOB!!!", True, (255,127,80))
            ANYKEYS = fontS.render("Press any key to quit", True, (0, 128, 0))
            screen.blit(WIN,(resolution[0]/2 - WIN.get_width() // 2, resolution[0]/2.5 - WIN.get_height() // 2))
            screen.blit(ANYKEYS,(resolution[0]/2 - ANYKEYS.get_width() // 2, resolution[0]/2 - ANYKEYS.get_height() // 2))

        pygame.display.update()
        FPSCLOCK.tick(60)


if __name__ == "__main__":
    '''
    # Game loop
    stat, level = startMenu()
    print(stat[0])
    print(level)

    if stat[0]:
        # maze
        resolution = (850, 850)
        current_position = [0, 1]
        score = 0
        enemy_num = 0
        enemies = []

        if level=='easy':
            maze = maze_gen(6, 6)
            object_size = (37, 37)
            cell_margin = 0.5
            # pink white
            cell_colors = (255, 192, 203), (255, 255, 255)
        elif level=='medium':
            maze = maze_gen(10, 10)
            object_size = (30, 30)
            cell_margin = 0.5
            # green white
            cell_colors = (144,238,144),(255, 255, 255)
            #enemy_position = find_random_spot(maze)
            enemy_num = 1
        elif level=='hard':
            maze = maze_gen(18, 18)
            object_size = (20, 20)
            cell_margin = 0.5
            # blue white
            cell_colors = (0,191,255), (255, 255, 255)
            #enemy_position = find_random_spot(maze)
            enemy_num = 2
        elif level=='insane':
            maze = maze_gen(26, 26)
            object_size = (15, 15)
            cell_margin = 0.5
            # red white
            cell_colors = (220,20,60), (169,169,169)
            enemy_num = 5

        for i in range(enemy_num):
            #print(i)
            enemies.append(find_random_spot(maze))

        main(level, enemies)
    '''
    #levels = ['easy', 'medium', 'hard', 'insane']
    #stat = [0]
    #level = levels[1]
    #win = 0

    #if win==0:
    print('StartMenu')
    stat, level = startMenu()
    #print(stat, level)

    if stat[0]:
        # maze
        resolution = (850, 850)
        current_position = [0, 1]
        score = 0
        enemy_num = 0
        enemies = []

        #if win and level!="insane":
        #    level = levels[levels.index(level) + 1]
        if(stat[0] == 2):
            temp = read_maze()

            if(temp != 0):
                maze = temp[0]
                level = temp[1]
                current_position = temp[2]


        if level=='easy':
            if(stat[0] == 1):
                maze = maze_gen(6, 6)
            
            object_size = (37, 37)
            cell_margin = 0.5
            # pink white
            cell_colors = (255, 192, 203), (255, 255, 255), (255, 255, 0)
        elif level=='medium':
            if(stat[0] == 1):
                maze = maze_gen(10, 10)

            object_size = (30, 30)
            cell_margin = 0.5
            # green white
            cell_colors = (144,238,144), (255, 255, 255), (255, 255, 0)
            #enemy_position = find_random_spot(maze)
            enemy_num = 2
        elif level=='hard':
            if(stat[0] == 1):
                maze = maze_gen(18, 18)

            object_size = (20, 20)
            cell_margin = 0.5
            # blue white
            cell_colors = (0,191,255), (255, 255, 255), (255, 255, 0)
            #enemy_position = find_random_spot(maze)
            enemy_num = 5
        elif level=='insane':
            if(stat[0] == 1):
                maze = maze_gen(26, 26)

            object_size = (15, 15)
            cell_margin = 0.5
            # red white
            cell_colors = (220,20,60), (169,169,169), (0, 0, 0)
            enemy_num = 10

        

        for i in range(enemy_num):
            #print(i)
            #enemies.append(find_random_spot(maze))
            enemies.append(find_spot_center(maze))

        main(level, enemies)
        print('end')
   

    
    pygame.quit()
    
    sys.exit()