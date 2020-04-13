import random

def distance(x1, x2):
    return ((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2)**0.5

def delete_random_surround_wall(maze, pos):
    total = len(maze) * len(maze[0])
    count = 0
    while 1:
        if count == total:
            break
        r = random.randint(1,len(maze)-2)
        c = random.randint(1,len(maze[r])-2)
        count += 1
        if maze[r][c] == 0 and distance([c,r], pos)==1.0:
            #print(distance([c,r], pos))
            break
    maze[r][c] = 1

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

def clear_path(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (maze[row][col] == 2):
                maze[row][col] = 1;
