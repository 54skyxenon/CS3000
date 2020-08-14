#!/usr/local/bin/python3
# Author: Brandon Liang

import random

# helper to remove a node and its edges from the graph


def drop(graph, node):
    newGraph = dict((v, set()) for v in graph if v != node)
    for u in graph.keys() - {node}:
        for v in graph[u]:
            if v != node:
                newGraph[u].add(v)

    return newGraph

# Using Bounded Search Tree to check for existence a k-sized vertex cover
# This problem is fixed parameter tractable, with a runtime of O(2^k * m)


def bstvc(graph, k):
    E = sum([len(graph[v]) for v in graph]) // 2

    if E == 0:
        return True
    elif k == 0:
        return False
    else:
        # Pick a random edge (u, v) of graph
        u = random.choice([k for k in graph.keys() if len(graph[k]) > 0])
        v = random.choice(list(graph[u]))
        a = bstvc(drop(graph, u), k - 1)
        b = bstvc(drop(graph, v), k - 1)
        return a or b


graphExample = dict()
graphExample['A'] = {'B', 'C', 'E'}
graphExample['B'] = {'A', 'C', 'D', 'F'}
graphExample['C'] = {'A', 'B', 'D', 'E', 'F'}
graphExample['D'] = {'B', 'C', 'F'}
graphExample['E'] = {'A', 'C'}
graphExample['F'] = {'B', 'C', 'D'}

assert not bstvc(graphExample, 2)
assert bstvc(graphExample, 4)
