ALL = bin/maze-gen

all: $(ALL)

CFLAGS = -Iinclude -Wall -Wextra -std=c++11

clean: 
	rm -f a.out obj/* bin/*

# Object files

OBJS = obj/disjoint-height.o obj/disjoint-rank.o obj/disjoint-size.o

obj/disjoint-height.o: src/disjoint-height.cpp include/disjoint.hpp
	g++ $(CFLAGS) -c -o obj/disjoint-height.o src/disjoint-height.cpp

obj/disjoint-rank.o: src/disjoint-rank.cpp include/disjoint.hpp
	g++ $(CFLAGS) -c -o obj/disjoint-rank.o src/disjoint-rank.cpp

obj/disjoint-size.o: src/disjoint-size.cpp include/disjoint.hpp
	g++ $(CFLAGS) -c -o obj/disjoint-size.o src/disjoint-size.cpp

obj/maze-gen.o: src/maze-gen.cpp include/disjoint.hpp
	g++ $(CFLAGS) -c -o obj/maze-gen.o src/maze-gen.cpp

# Executables

bin/maze-gen: obj/maze-gen.o $(OBJS)
	g++ -O -o bin/maze-gen obj/maze-gen.o $(OBJS)