/* disjoint_by_height.cpp
   Union by Height implementation of Disjoint Sets.
   James S. Plank
   Tue Sep 25 15:51:14 EDT 2018
 */

#include <vector>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include "disjoint.hpp"
using namespace std;

DisjointSetByHeight::DisjointSetByHeight(int nelements)
{
  links.resize(nelements, -1);
  heights.resize(nelements, 1);
}

int DisjointSetByHeight::Union(int s1, int s2)
{
  int p, c;

  if (links[s1] != -1 || links[s2] != -1) {
    cerr << "Must call union on a set, and not just an element.\n";
    exit(1);
  }

  if (heights[s1] > heights[s2]) {
    p = s1;
    c = s2;
  } else {
    p = s2;
    c = s1;
  }
  
  links[c] = p;
  if (heights[p] == heights[c]) heights[p]++;
  return p;
}

int DisjointSetByHeight::Find(int element)
{
  while (links[element] != -1) element = links[element];
  return element;
}

void DisjointSetByHeight::Print() const
{
  size_t i;

  printf("\n");
  printf("Node:  ");
  for (i = 0; i < links.size(); i++) printf("%3lu", i);  
  printf("\n");

  printf("Links: ");
  for (i = 0; i < links.size(); i++) printf("%3d", links[i]);  
  printf("\n");

  printf("Hghts: ");
  for (i = 0; i < links.size(); i++) printf("%3d", heights[i]);  
  printf("\n\n");
}