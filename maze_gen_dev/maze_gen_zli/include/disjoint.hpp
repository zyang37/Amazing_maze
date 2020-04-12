/* disjoint.hpp
   Interface and subclass specification for disjoint sets.
   James S. Plank
   Tue Sep 25 15:48:18 EDT 2018
 */

#pragma once
#include <vector>

/* The Disjoint Set API is implemented as a c++ interface, 
   because I am implementing it three ways.  Each subclass
   implementation is in its own cpp file. */

class DisjointSet {
  public:
    virtual ~DisjointSet() {};
    virtual int Union(int s1, int s2) = 0;
    virtual int Find(int element) = 0;  
    virtual void Print() const = 0;
};

/* The first subclass implements Union-by-Size. */

class DisjointSetBySize : public DisjointSet {
  public:
    DisjointSetBySize(int nelements);
    int Union(int s1, int s2);
    int Find(int element); 
    void Print() const ;

  protected:
    std::vector <int> links;
    std::vector <int> sizes;
};

/* The second subclass implements Union-by-Height. */

class DisjointSetByHeight : public DisjointSet {
  public:
    DisjointSetByHeight(int nelements);
    int Union(int s1, int s2);
    int Find(int element); 
    void Print() const;

  protected:
    std::vector <int> links;
    std::vector <int> heights;
};

/* The third subclass implements Union-by-Rank with path compression. */

class DisjointSetByRankWPC : public DisjointSet {
  public:
    DisjointSetByRankWPC(int nelements);
    int Union(int s1, int s2);
    int Find(int element); 
    void Print() const;

  protected:
    std::vector <int> links;
    std::vector <int> ranks;
};