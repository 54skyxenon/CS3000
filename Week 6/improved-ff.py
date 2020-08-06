#!/usr/local/bin/python3
# Author: Brandon Liang

# so we can use heapdict
import sys
import os
sys.path.append(os.path.abspath('../Week 4'))

from collections import defaultdict
from heapdict import maxHeapdict

# DIFFERENCE: We'll select a smart augmented path this time
# Two methods: fattest path and shortest path

def fattestPath(network, start, end):
    # Let Q be a new max heap
    Q = maxHeapdict((u, float('-inf') if u != start else float('inf')) for u in network)
    lookup = maxHeapdict((u, float('-inf') if u != start else float('inf')) for u in network)
    parent = dict((v, None) for v in network)
        
    while Q:
        # pop the largest item
        u, width = Q.popitem()
        for v in network[u]:
            alt = max(lookup[v], min(lookup[u], network[u][v]))
            if alt > lookup[v]:
                Q[v] = alt
                lookup[v] = alt
                parent[v] = u
                    
    path = [end]
    while parent[path[0]]:
        path = [parent[path[0]]] + path
    return path

def shortestPath(network, start, end):
    pass

def fordFulkerson(network):
    residual = defaultdict(dict)
    for u in network:
        for v in network[u]:
            residual[u][v] = network[u][v]
            residual[v][u] = 0

    # get rid of all zero edges on residual graph, so Dijkstra's doesn't die
    def dropZeroEdges(network):
        result = dict((v, dict()) for v in network)

        for u in network:
            for v in network[u]:
                if network[u][v] > 0:
                    result[u][v] = network[u][v]

        return result

    maxFlow = float('-inf')
    while True:
        augmentingPath = fattestPath(dropZeroEdges(residual), 's', 't')

        augment = float('inf')
        for i in range(len(augmentingPath) - 1):
            first = augmentingPath[i]
            second = augmentingPath[i + 1]
            augment = min(augment, residual[first][second])

        # no more augmenting paths
        if augment == float('inf'):
            return maxFlow

        for i in range(len(augmentingPath) - 1):
            first = augmentingPath[i]
            second = augmentingPath[i + 1]
            residual[first][second] -= augment
            residual[second][first] += augment

        maxFlow = max(maxFlow, sum([residual['t'][node] for node in residual['t'] ]))

networkExample1 = dict()
networkExample1['s'] = {'1': 20, '2': 10}
networkExample1['1'] = {'2': 30, 't': 10}
networkExample1['2'] = {'t': 20}
networkExample1['t'] = set()

networkExample2 = dict()
networkExample2['s'] = {'2': 10, '3': 10}
networkExample2['2'] = {'3': 2, '5': 8, '4': 4}
networkExample2['3'] = {'5': 9}
networkExample2['4'] = {'t': 10}
networkExample2['5'] = {'4': 6, 't': 10}
networkExample2['t'] = set()

networkExample3 = dict()
networkExample3['s'] = {'2': 10, '3': 5, '4': 15}
networkExample3['2'] = {'5': 9, '6': 15, '3': 14}
networkExample3['3'] = {'6': 8, '4': 4}
networkExample3['4'] = {'7': 30}
networkExample3['5'] = {'6': 15, 't': 10}
networkExample3['6'] = {'7': 15, 't': 10}
networkExample3['7'] = {'3': 6, 't': 10}
networkExample3['t'] = set()

print('Max flow 1: {}'.format(fordFulkerson(networkExample1)))
print('Max flow 2: {}'.format(fordFulkerson(networkExample2)))
print('Max flow 3: {}'.format(fordFulkerson(networkExample3)))