import random

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
    while 1:
        x = random.randint(-1,1)
        y = random.randint(-1,1)
        if x==0 or y==0:
            break
    return (x, y)
