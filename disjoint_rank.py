"""
disjoint_by_rank.py
Union by Rank with Path Compression implementation of Disjoint Sets.
Zhouyang Li
03/16/2020
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

class DisjointSetByRankWPC:

    links = list()
    ranks = list()

    def __init__(self, nelements):
        self.links = []
        self.ranks = []
        for i in range(nelements):
            self.links.append(-1)
            self.ranks.append(1)

    def Union(self, s1, s2):
        if self.links[s1] == -1 and self.links[s2] == -1:
            if self.ranks[s1] > self.ranks[s2]:
                p = s1;
                c = s2;
            else:
                p = s2;
                c = s1;

            self.links[c] = p;
            if self.ranks[p] == self.ranks[c]:
                self.ranks[p] += 1
            return p

    def Find(self, e):
        """
        Find the root of the tree, but along the way, set
        the parents' links to the children.
        """
        c = -1;
        #try:
        while self.links[e] != -1:
            p = self.links[e]
            self.links[e] = c
            c = e
            e = p
        #except:
        #    return -1

        """
        Now, travel back to the original element, setting
        every link to the root of the tree.
        """
        p = e
        e = c
        while e != -1:
            c = self.links[e]
            self.links[e] = p
            e = c

        return p

    def PrintDisjointSet(self):
        print('Node:  ', end = "")

        for i in range(len(self.links)):
            print("%3d" % i, end = " ")
        print('\n', end = "")

        print('Links: ', end = "")
        for i in range(len(self.links)):
            print("%3d" % self.links[i], end = " ")
        print('\n', end = "")

        print('Ranks: ', end = "")
        for i in range(len(self.ranks)):
            print("%3d" % self.ranks[i], end = " ")
        print('\n', end = "")


if __name__ == '__main__':
    """
    Example of Use
    Example comes from Plank's notes: http://web.eecs.utk.edu/~jplank/plank/classes/cs302/Notes/Disjoint/
    """
    d = DisjointSetByRankWPC(10)
    d.PrintDisjointSet()
    s01 = d.Union(0, 1)
    s23 = d.Union(2, 3)
    s45 = d.Union(4, 5)
    d.PrintDisjointSet()
    print(d.Find(0), d.Find(1))

    s0123 = d.Union(s01, s23);
    s456 = d.Union(s45, 6);
    s4567 = d.Union(s456, 7);
    s45678 = d.Union(s4567, 8);
    d.PrintDisjointSet()

    print(d.Find(1), d.Find(2), d.Find(4), d.Find(7))
    d.PrintDisjointSet()

    s012345678 = d.Union(s0123, s45678)
    d.PrintDisjointSet()

    print(d.Find(3));
    print(d.Find(5));
    print(d.Find(7));
    d.PrintDisjointSet();

    print(d.Find(0));
    d.PrintDisjointSet();

    print(d.Find(4));
    print(d.Find(6));
    print(d.Find(8));
    d.PrintDisjointSet();
