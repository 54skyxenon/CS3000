#!/usr/local/bin/python3
# Author: Brandon Liang

# so we can use heapdict
import sys
import os
sys.path.append(os.path.abspath('../Week 4'))

from collections import defaultdict
from heapdict import heapdict
import random

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
                                safeEdge = ((u, v), components[ccIndex], graph[u][v], ccIndex)
            
            cut |= safeEdge[1]
            T |= {safeEdge[0]}
            newComponents.append(cut)
            del components[safeEdge[3]]

        components = newComponents

    return T

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

def kruskal(graph):
    T = set()

    edges = list()
    for u in graph:
        for v in graph[u]:
            edges.append((u, v))
            edges.append((v, u))
    
    edges.sort(key=lambda x: graph[x[0]][x[1]])
    print('edges: {}'.format(str(edges)))

    # TODO

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

print(genericMST)
print(boruvkaMST)
print(primMST)
print(kruskalMST)

# are the edges the same for all four algorithms (order and direction don't matter)
assert set([tuple(sorted(elt)) for elt in genericMST]) == set([tuple(sorted(elt)) for elt in boruvkaMST])
assert set([tuple(sorted(elt)) for elt in boruvkaMST]) == set([tuple(sorted(elt)) for elt in primMST])
assert set([tuple(sorted(elt)) for elt in primMST]) == set([tuple(sorted(elt)) for elt in kruskalMST])