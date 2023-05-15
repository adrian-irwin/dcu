#!/usr/bin/env python3

import sys


class Graph(object):

    def __init__(self, V, ):
        self.V = V
        self.adj = {}  # we use this to map vertices to their neighbours
        for v in range(V):
            self.adj[v] = list()  # the list of nodes which node v connects to is empty

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degree(self, v):
        return len(self.adj[v])

    def maxDegree(self):
        return max([self.degree(v) for v in self.adj])  # [4, 1, 1, 2, 3, 3, 2]

    def averageDegree(self):
        return sum([self.degree(v) for v in self.adj]) / self.V


def main():
    with open("graph01.txt") as f:
        V = int(f.readline())
        g = Graph(V)

        print(g.adj)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    print(g.adj)

    print(g.degree(0))
    print(g.degree(2))

    print(g.maxDegree())

    print(g.averageDegree())


if __name__ == '__main__':
    main()
