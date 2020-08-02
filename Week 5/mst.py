#!/usr/local/bin/python3
# Author: Brandon Liang

# so we can use heapdict
import sys
import os
sys.path.append(os.path.abspath('../Week 4'))

import random
from heapdict import heapdict
from collections import defaultdict

# Five algorithms for computing the minimal spanning tree of a connected, weighted, undirected graph are:
# GenericMST, Boruvka's, Prim's, Kruskal's and Reverse Kruskal (which wasn't gone over in class)

# The "Only" MST Algorithm
def generic(graph):
    A = set()

    # we have a spanning tree if all vertices are in A
    def isSpanningTree(edges):
        return set(sum(edges, ())) == graph.keys()

    # find an edge (u, v) that is safe for set A
    while not isSpanningTree(A):
        safeEdge = (None, float('inf'))

        cut = set(sum(A, ()))
        # initially, no nodes are in the cut so we have to randomly pick one
        if not cut:
            cut = {random.choice(list(graph.keys()))}

        for u in cut:
            for v in graph[u].keys() - cut:
                if graph[u][v] < safeEdge[1]:
                    safeEdge = ((u, v), graph[u][v])

        A |= {safeEdge[0]}

    return A

# Limitation: all edge weights must be distinct
# Loop through all components and select min-weighted edge connecting to another component => O(m log n)
def boruvka(graph):
    T = set()

    # Let C_1, C_2, ..., C_k be the connected components of (V, T)
    components = [{key} for key in graph.keys()]

    # This main loop takes O(log n)
    while len(components) > 1:
        newComponents = list()

        while components:
            cut = components.pop()
            # (safe edge itself, connected component to union, min distance, index of cc to union)
            safeEdge = (None, None, float('inf'), -1)

            for u in cut:
                for v in graph[u].keys() - cut:
                    if graph[u][v] < safeEdge[2]:
                        # union whichever connected component contains the neighbor
                        for ccIndex in range(len(components)):
                            if v in components[ccIndex]:
                                safeEdge = (
                                    (u, v), components[ccIndex], graph[u][v], ccIndex)

            cut |= safeEdge[1]
            T |= {safeEdge[0]}
            newComponents.append(cut)
            del components[safeEdge[3]]

        components = newComponents

    return T

# Basic idea is to join shortest edge from all connected nodes, starting with a single random node => O(m log n)
def prim(graph):
    # let Q be a priority queue storing V
    Q = heapdict((v, float('inf')) for v in graph)

    # arbitrary start node
    s = random.choice(list(graph.keys()))
    Q[s] = 0

    last = dict((v, None) for v in graph)

    while Q:
        u = Q.popitem()[0]
        for v in graph[u]:
            if v in Q and graph[u][v] < Q[v]:
                Q[v] = graph[u][v]
                last[v] = u

    # excluding s
    T = set()
    for v in last:
        if last[v]:
            T |= {(v, last[v])}
    return T

# Quick and dirty singly linked list class that supports O(1) time unions for Kruskal
class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

        if next:
            self.end = next.end
        else:
            self.end = self

    def iter(self):
        iterable = list()

        ptr = self
        while ptr:
            iterable.append(ptr.data)
            ptr = ptr.next

        return iterable

    def joinAtEnd(self, other):
        self.end.next = other
        self.end = other.end

# Sort edges then add shortest edge not making a cycle at each step => O(m log m)
def kruskal(graph):
    T = set()

    find, union = dict(), dict()

    index = 1
    for node in graph:
        find[node] = index
        union[index] = LinkedList(node)
        index += 1
    
    edges = list()
    for u in graph:
        for v in graph[u]:
            edges.append((u, v))
            edges.append((v, u))

    edges.sort(key=lambda x: graph[x[0]][x[1]])

    for e in edges:
        u, v, w = e[0], e[1], graph[e[0]][e[1]]

        if find[u] != find[v]:
            T |= {(u, v)}
            union[find[u]].joinAtEnd(union[find[v]])
            for node in union[find[u]].iter():
                find[node] = find[u]

    return T

graphExample1 = defaultdict(dict)
graphExample1['A'] = {'F': 6, 'E': 5, 'C': 8, 'B': 14}
graphExample1['B'] = {'A': 14, 'C': 3}
graphExample1['C'] = {'B': 3, 'A': 8, 'D': 10}
graphExample1['D'] = {'C': 10, 'E': 7, 'G': 15}
graphExample1['E'] = {'A': 5, 'F': 12, 'D': 7, 'H': 9}
graphExample1['F'] = {'A': 6, 'E': 12}
graphExample1['G'] = {'D': 15}
graphExample1['H'] = {'E': 9}

genericMST = generic(graphExample1)
boruvkaMST = boruvka(graphExample1)
primMST = prim(graphExample1)
kruskalMST = kruskal(graphExample1)

# are the edges the same for all four algorithms (order and direction don't matter)
def orderedMST(mst):
    return set([tuple(sorted(edge)) for edge in mst])

assert orderedMST(genericMST) == orderedMST(boruvkaMST)
assert orderedMST(boruvkaMST) == orderedMST(primMST)
assert orderedMST(primMST) == orderedMST(kruskalMST)

print('MST edges: {}'.format(kruskalMST))
