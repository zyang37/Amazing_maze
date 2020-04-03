import random
from disjoint_rank import *

def maze_gen(r, c):
    maze = []

    # Initialize the maze
    row = [1]*(r*2-1)
    col = [row]*(c*2-1)
    maze = col

    for i in range(len(maze)):
        if i%2 == 1:
            maze[i] = [0 for val in maze[i]]
        else:
            for j in range(len(maze[i])):
                if j%2 == 1:
                    maze[i][j] = 0

    walls = []
    d = DisjointSetByRankWPC(r*c)

    for row in range(r-1):
        for col in range(c):
            c1 = row*c + col
            walls.append(c1)

    for row in range(r):
        for col in range(c-1):
            c1 = (row*c + col) + r*c
            walls.append(c1)

    ncomp = r*c;
    count = 0
    while ncomp > 1:
        count += 1
        if count == r*c:
            break
        c1 = random.choice(walls)
        tmp = c1
        if (c1 < r*c):
            c2 = c1 + c
            row1 = int(c1 / c);
            column1 = c1 % c;
            maze_row = 2 * row1 + 1;
            maze_colume = 2 * column1;
        else:
            c1 = c1 - r*c
            c2 = c1 + 1
            row1 = int(c1 / c);
            column1 = c1 % c;
            maze_row = 2 * row1;
            maze_colume = 2 * column1 + 1;

        s1 = d.Find(c1)
        s2 = d.Find(c2)
        if s1 != s2:
            d.Union(s1, s2)
            walls.remove(tmp)
            #print(int(maze_row), int(maze_colume))
            maze[maze_row][maze_colume] = 1;
            ncomp = ncomp - 1
        else:
            continue

    maze.insert(0, [0]*len(maze[0]))
    maze.append([0]*len(maze[0]))

    for i in range(len(maze)):
        temp = maze[i][:]
        temp.insert(0, 0)
        temp.append(0)
        maze[i] = temp

    maze[1][0] = 1
    maze[-2][-1] = 1

    return maze
