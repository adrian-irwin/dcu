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
        # we never want to visit the same node twice
        # so we need to remember where we have been
        # so we do not go there again
        # the visited list records where we have been
        # to start with we have not visited anywhere
        self.visited = [False for _ in range(g.V)]
        # we want to record how we reached each node
        # really which node we came from to reach a given node
        self.parent = [False for _ in range(g.V)]
        # start exploring from node s!
        self.dfs(s)

    # the magic
    def dfs(self, v):
        # we are at node v,
        # if we are at node v then we have visited it
        self.visited[v] = True
        # where can we go from node v?
        # for each node w that is connected directly to v
        for w in self.g.adj[v]:
            # have we been to w before
            # if not then go there (if we have been there ignore it)
            if not self.visited[w]:
                # let's record how we got to w
                self.parent[w] = v
                # let's go to w and continue from there
                self.dfs(w)

    # Return True if there is a path from s to v
    def hasPathTo(self, v):
        return self.visited[v]

    # Return path from s to v (or None should one not exist)
    def pathTo(self, v):
        if self.hasPathTo(v):
            path = [v]
            while v != self.s:
                v = self.parent[v]
                path.append(v)
            return path[::-1]
        else:
            return None


def main():
    with open('graph01.txt') as f:
        V = int(f.readline())

        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

        # do a DFS on g starting at vertex 0
        # paths now contains the results of the DFS
        paths = DFSPaths(g, 0)

        # print the two lists that we built
        print(paths.visited)
        print(paths.parent)

        print(paths.hasPathTo(6))
        # Should print True

        print(paths.pathTo(6))
        # Should print [0, 5, 3, 4, 6]


if __name__ == '__main__':
    main()
