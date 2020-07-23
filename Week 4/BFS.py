#!/usr/local/bin/python3
# Author: Brandon Liang

from collections import defaultdict, deque

# BFS - Breadth-First Search
# Time complexity: O(n + m), where n = number of vertices and m = number of edges

# run BFS on a given start node in the graph
# give back path taken and which layers nodes were found in BFS, inf means not found
def BFS(graph, startNode):
    found = {startNode}
    path = []
    layers = dict((node, float('inf')) for node in graph)

    # two-element tuples represent node and node layer
    queue = deque()
    queue.append((startNode, 0))

    while queue:
        nextNode = queue.popleft()
        path.append(nextNode[0])
        layers[nextNode[0]] = nextNode[1]

        for neighbor in graph[nextNode[0]]:
            if neighbor not in found:
                queue.append((neighbor, nextNode[1] + 1))
                found |= {neighbor}

    return path, layers

# we will use the adjacency list representation
undirectedExample = defaultdict(set)
undirectedExample[1] = {2, 3}
undirectedExample[2] = {1, 3, 5, 4}
undirectedExample[3] = {1, 2, 5, 7, 8}
undirectedExample[4] = {2, 5}
undirectedExample[5] = {4, 2, 3, 6}
undirectedExample[6] = {5}
undirectedExample[7] = {3, 8}
undirectedExample[8] = {3, 7}
undirectedExample[9] = {10}
undirectedExample[10] = {9}
undirectedExample[11] = {12}
undirectedExample[12] = {11, 13}
undirectedExample[13] = {12}

exPath, exLayers = BFS(undirectedExample, 1)
print('\nStarting from 1 on undirected graph example: ')
print(exPath)
print(str(exLayers) + '\n')

directedExample = defaultdict(set)
directedExample[1] = {2, 3}
directedExample[2] = {3}
directedExample[4] = {3}

exPath, exLayers = BFS(directedExample, 1)
print('Starting from 1 on directed graph example: ')
print(exPath)
print(str(exLayers) + '\n')