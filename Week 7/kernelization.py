#!/usr/local/bin/python3
# Author: Brandon Liang

import importlib
bstvc = importlib.import_module('bst-vc').bstvc
drop = importlib.import_module('bst-vc').drop

# We can optimize the our bounded search tree algorithm through kernelization
# Meaning: we'll preprocess the graph to remove nodes with > k neighbors
# The idea is that any node with > k neighbors has to be in any yes solution

# This runs in O(k^2 * 2^k + kn + m) time, a big improvement than without kernelization

def bstWithKernel(graph, k):
    def moreThanKNeighbors():
        for v in graph:
            if len(graph[v]) > k:
                return v

        return None

    C = set()
    while moreThanKNeighbors():
        v = moreThanKNeighbors()
        C.add(v)
        graph = drop(graph, v)
        k -= 1
        if k < 0:
            return False

    # C unioned with the bst-vc procedure on the remaining graph is the solution
    return bstvc(graph, k)


graphExample1 = dict()
graphExample1['A'] = {'B', 'C', 'D'}
graphExample1['B'] = {'A'}
graphExample1['C'] = {'A'}
graphExample1['D'] = {'A'}

assert bstWithKernel(graphExample1, 2)

graphExample2 = dict()
graphExample2['a'] = {'b', 'c', 'h', 'g', 'd'}
graphExample2['b'] = {'a', 'c', 'h', 'k'}
graphExample2['c'] = {'a', 'b', 'h', 'j'}
graphExample2['d'] = {'a', 'j', 'f', 'l'}
graphExample2['e'] = {'h', 'i', 'f'}
graphExample2['f'] = {'e', 'd', 'k', 'l'}
graphExample2['g'] = {'a', 'i', 'l', 'j'}
graphExample2['h'] = {'a', 'b', 'c', 'e'}
graphExample2['i'] = {'e', 'l', 'g'}
graphExample2['j'] = {'c', 'k', 'd', 'g'}
graphExample2['k'] = {'b', 'f', 'j'}
graphExample2['l'] = {'f', 'd', 'i', 'g'}

assert not bstWithKernel(graphExample2, 3)
assert bstWithKernel(graphExample2, 10)