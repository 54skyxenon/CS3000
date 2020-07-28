#!/usr/local/bin/python3
# Author: Brandon Liang

from collections import defaultdict
from heapdict import heapdict

# Dijkstra's single-source shortest path algorithm

# n = number of vertices 
# m = number of edges

# Dijkstra's without using heap - O(n^2 + m) time
def dijkstraNaive(graph, start):
    dists = dict((node, float('inf')) for node in graph)
    dists[start] = 0
    parents = dict((node, None) for node in graph)

    # Q holds the unexplored nodes
    Q = graph.keys()

    while Q:
        # Find closest unexplored
        u = (None, float('inf'))
        for w in Q:
            if dists[w] < u[1]:
                u = (w, dists[w])

        u = u[0]
        Q -= {u}

        # Update the outneighbors of u
        for v in (graph[u].keys() & Q):
            if dists[v] > dists[u] + graph[u][v]:
                dists[v] = dists[u] + graph[u][v]
                parents[v] = u
    
    return dists, parents

# Dijkstra's with a heap - O(n log n + m log n) time
def dijkstra(graph, start):
    dists = dict((node, float('inf')) for node in graph)
    lookups = dict((node, float('inf')) for node in graph)

    dists[start] = 0
    lookups[start] = 0

    parents = dict((node, None) for node in graph)
    
    # Let Q be a new heap
    Q = heapdict()
    Q[start] = 0
    for u in (graph.keys() - {start}):
        Q[u] = float('inf')

    while Q:
        # extract min
        u, dists[u] = Q.popitem()

        # consider outneighbors
        for v in (graph[u].keys() & Q):
            dists[v] = lookups[v]
            
            if dists[v] > dists[u] + graph[u][v]:
                Q[v] = dists[u] + graph[u][v]
                lookups[v] = dists[u] + graph[u][v]
                parents[v] = u

    return dists, parents

graphExample1 = defaultdict(dict)
graphExample1['A'] = {'B': 10, 'C': 3}
graphExample1['B'] = {'C': 1, 'D': 2}
graphExample1['C'] = {'B': 4, 'D': 8, 'E': 2}
graphExample1['D'] = {'E': 7}
graphExample1['E'] = {'D': 9}

graphExample2 = defaultdict(dict)
graphExample2['A'] = {'B': 2, 'C': 5}
graphExample2['B'] = {'C': 2, 'D': 5}
graphExample2['C'] = {'B': 1, 'D': 2, 'E': 1}
graphExample2['D'] = {'E': 3}
graphExample2['E'] = {'D': 6}

# fails with negative weights
graphExample3 = defaultdict(dict)
graphExample3['S'] = {'A': 5, 'B': 2}
graphExample3['A'] = {'B': -7}
graphExample3['B'] = {}

assert dijkstraNaive(graphExample1, 'A') == dijkstra(graphExample1, 'A')
assert dijkstraNaive(graphExample2, 'A') == dijkstra(graphExample2, 'A')
assert dijkstraNaive(graphExample3, 'S') == dijkstra(graphExample3, 'S')
print(dijkstra(graphExample1, 'A'))
print(dijkstra(graphExample2, 'A'))
print(dijkstra(graphExample3, 'S'))

