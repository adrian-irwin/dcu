#!/usr/bin/env python3
import sys


class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


class DFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False for _ in range(g.V)]
        self.parent = [False for _ in range(g.V)]
        self.dfs(s)

    def dfs(self, v):
        self.visited[v] = True
        for w in self.g.adj[v]:
            if not self.visited[w]:
                self.parent[w] = v
                self.dfs(w)

    def hasPathTo(self, v):
        return self.visited[v]


def main():
    f = sys.stdin
    V = int(f.readline())
    g = Graph(V)
    for line in f:
        v, w = [int(t) for t in line.strip().split()]
        g.addEdge(v, w)

    allPaths = {}
    for i in range(V):
        allPaths[i] = DFSPaths(g, i)

    allIslands = []
    for i in range(V):
        allIslands.append([])
        for j in range(V):
            if allPaths[i].hasPathTo(j):
                allIslands[i].append(j)

    islands = []
    for x in allIslands:
        if x not in islands:
            islands.append(x)
    print(len(islands))


if __name__ == '__main__':
    main()
