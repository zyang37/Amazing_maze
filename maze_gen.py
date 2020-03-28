import random

from disjoint_rank import DisjointSetByRankWPC

'''
void rand_maze {
  // begin with a rectangular maze of all closed cells
  // numrows = number of rows of cells;
  // numcols = number of columns of cells;
  start = cell at (0,0);
  goal  = cell at (numrows-1, numcols-1);
  numcells = numrows * numcols;
  Partition p(numcells); // p represents the maze components

  // goal is not reachable from start
  while (!p.Find(start, goal)) {
    edge = randomly select a wall;
    x = edge.x;
    y = edge.y;
    if(!p.Find(x,y)) {
      remove edge;
      // x and y now in same component
      p.Union(x,y);
    }
  }
}
'''
class grid:
    def __init__(self, size=0):
        self.size = size
        self.grid = [0] * self.size
        #print(self.grid)

    def get_rand_loc(self):
        x = random.randint(0, self.size-1)
        return x

    def set_one(self, i):
        print(i)
        self.grid[i] = 1


def maze_gen(numrows, numcols):
    start = 0
    numcells = numrows * numcols
    goal  = numcells - 1
    g = grid(numcells)
    p = DisjointSetByRankWPC(numcells)

    while p.Find(start) != goal:
        x = g.get_rand_loc()
        y = g.get_rand_loc()
        if p.Find(x) != y:
            g.set_one(x)
            g.set_one(y)
            p.Union(x,y)

    return g.grid


if __name__ == '__main__':
    m = maze_gen(3,3)
    print(m)
