#include <vector>
#include <cstdlib>
#include <cstdio>
#include <map>
#include "disjoint.hpp"
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
  int r, c, row, column, c1, c2, ncomp, s1, s2, hov;
  int row1, column1, maze_row, maze_colume;
  DisjointSet *d;
  map <double, int> walls;
  map <double, int>::iterator wit;
  map <double, int>::iterator tmp;
  vector<vector<char>> maze;

  /* Parse the command line and create the instance of the disjoint set. */

  if (argc != 4) { 
    fprintf(stderr, "usage mazegen rows cols size|height|rank\n"); exit(1); }
  
  r = atoi(argv[1]);
  c = atoi(argv[2]);

  switch(argv[3][0]) {
    case 's': d = new DisjointSetBySize(r*c); break;
    case 'h': d = new DisjointSetByHeight(r*c); break;
    case 'r': d = new DisjointSetByRankWPC(r*c); break;
    default: fprintf(stderr, "Bad last argument.  Should be s|h|r.\n"); exit(1);
  }

  /* Initialize the maze */
  maze.resize(2 * r - 1, vector<char>(2 * c - 1, '0'));

  for (row = 0; row < r - 1; row++) {
    for (column = 0; column < 2 * c - 1; column++) {
      maze[2 * row + 1][column] = '*';
    }
  }

  for (column = 0; column < c - 1; column++) {
    for (row = 0; row < 2 * r - 1; row++) {
      maze[row][2 * column + 1] = '*';
    }
  }

  /* Generate walls that separate vertical cells. */

  for (row = 0; row < r-1; row++) {
    for (column = 0; column < c; column++) {
      c1 = row*c + column;
      walls.insert(make_pair(drand48(), c1));
    }
  }

  /* Generate walls that separate horizontal cells. */

  for (row = 0; row < r; row++) {
    for (column = 0; column < c-1; column++) {
      c1 = (row*c + column) + r*c;
      walls.insert(make_pair(drand48(), c1));
    }
  }

  /* Run through the walls map, deleting walls when they
     separate cells in different disjoint sets. */

  ncomp = r*c;
  wit = walls.begin();
  while (ncomp > 1) {
    c1 = wit->second;
    if (c1 < r*c) {    // This is a wall separating vertical cells.
      c2 = c1 + c;
      row1 = c1 / c;
      column1 = c1 % c;
      maze_row = 2 * row1 + 1;
      maze_colume = 2 * column1;
    } else {           // This is a wall separating horizontal cells.
      c1 -= r*c;       // c1 and c2 are the two cells separated by the wall
      c2 = c1+1;
      row1 = c1 / c;
      column1 = c1 % c;
      maze_row = 2 * row1;
      maze_colume = 2 * column1 + 1;
    }
    s1 = d->Find(c1);
    s2 = d->Find(c2);
    if (s1 != s2) {     // Test for different connected components.
      d->Union(s1, s2);
      tmp = wit;
      wit++;
      walls.erase(tmp);
      maze[maze_row][maze_colume] = '0';
      ncomp--;
    } else {
      wit++;
    }
  }

  /* Print out the maze */
  for (row = 0; row < 2 * r - 1; row++) {
    for (column = 0; column < 2 * c - 1; column++) {
      cout << maze[row][column];
    }
    cout << endl;
  }


  /* Print out the remaining walls. */

  // printf("ROWS %d COLS %d\n", r, c);

  // for (wit = walls.begin(); wit != walls.end(); wit++) {
  //   c1 = wit->second;
  //   if (c1 < r*c) {
  //     c2 = c1 + c;
  //   } else {
  //     c1 -= r*c;
  //     c2 = c1+1;
  //   }
  //   printf("WALL %d %d\n", c1, c2);
  // }
  return 0;
}