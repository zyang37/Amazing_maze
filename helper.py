'''
Here are some helper functions
'''

import random

# Calculating the euclidean distance between two points
def distance(x1, x2):
    return ((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2)**0.5

# find a random wall that is near player, and remove it
def delete_random_surround_wall(maze, pos):
    total = len(maze) * len(maze[0])
    count = 0
    found = False
    temp = []
    while 1:
        if count == total:
            if len(temp)==0:
                temp.append([c,r])
            break
        r = random.randint(1,len(maze)-2)
        c = random.randint(1,len(maze[r])-2)
        count += 1

        if maze[r][c] == 0:
            if distance([c,r], pos)==1.0:
                #print(distance([c,r], pos))
                found = True
                break
            if distance([c,r], pos) <= 1.5:
                temp.append([c,r])
    if found:
        maze[r][c] = 1
    else:
        rp = random.choice(temp)
        maze[rp[1]][rp[0]] = 1
        print(distance([rp[1],rp[0]], pos))

# find a random wall within the current maze and remove it
def delete_random_wall(maze):
    total = len(maze) * len(maze[0])
    count = 0
    while 1:
        if count == total:
            break
        r = random.randint(1,len(maze)-2)
        c = random.randint(1,len(maze[r])-2)
        count += 1
        if maze[r][c] == 0:
            # print(r, c)
            break
    maze[r][c] = 1

def Arandom_move():
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    direction = random.choice(directions)
    return direction

# Hint Bell helper function
def show_path(maze, row, col):
    if (row == len(maze) - 1 and col == len(maze[0]) - 2 ):
        return True
    elif (row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0])):
        return False
    elif (maze[row][col] == 1):
        maze[row][col] = 2

        result = show_path(maze, row - 1, col) or show_path(maze, row + 1, col) or show_path(maze, row, col - 1) or show_path(maze, row, col + 1)

        if (result == False):
            maze[row][col] = 1

        return result

    else:
        return False

# after 5 sec will remove hint
def clear_path(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (maze[row][col] == 2):
                maze[row][col] = 1;

# helper function #1 for load game buttom
def save_game(maze, level, current_position):
    f = open("savedGame/save.txt","w+")

    #write the current position
    f.write("%d %d\r\n" % (current_position[0], current_position[1]))
    #write the difficulty level
    f.write("%s\r\n" % level)

    for i in maze:
        for j in i:
            f.write("%d " % j)
        f.write("\r\n")

# helper function #2 for load game buttom
def read_maze():
    maze = []

    f = open("savedGame/save.txt", "r")

    if f.mode != 'r':
        return 0

    current_position = [int(x) for x in f.readline()[:-1].split()]
    #print(current_position)
    level = f.readline()[:-1]

    f1 = f.readlines()


    for x in f1:
        temp = []
        for y in x.split():
            temp.append(int(y))

        maze.append(temp)


    return maze, level, current_position
