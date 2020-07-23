#!/usr/local/bin/python3
# Author: Brandon Liang

from collections import defaultdict

# DFS - Depth-First Search
# Time complexity: O(n + m), where n = number of vertices and m = number of edges
def DFS(graph, start, parents, explored):
    explored[start] = True

    for neighbor in graph[start]:
        if not explored[neighbor]:
            parents[neighbor] = start
            DFS(graph, neighbor, parents, explored)

    return parents

# postorder traversal, clock is a mutable singleton list
def postorder(graph, start, parents, explored, postorderVisits, clock):
    explored[start] = True

    for neighbor in sorted(graph[start]):
        if not explored[neighbor]:
            parents[neighbor] = start
            postorder(graph, neighbor, parents, explored, postorderVisits, clock)

    postorderVisits[start] = clock[0]
    clock[0] += 1

# preorder traversal, clock is a mutable singleton list
def preorder(graph, start, parents, explored, preorderVisits, clock):
    explored[start] = True
    
    preorderVisits[start] = clock[0]
    clock[0] += 1

    for neighbor in sorted(graph[start]):
        if not explored[neighbor]:
            parents[neighbor] = start
            preorder(graph, neighbor, parents, explored, preorderVisits, clock)

exampleGraph1 = defaultdict(set)
exampleGraph1['u'] = {'a', 'c'}
exampleGraph1['b'] = {'u'}
exampleGraph1['a'] = {'u'}
exampleGraph1['c'] = {'a', 'b'}

print('Regular DFS on example 1:')
print(DFS(exampleGraph1, 'u', 
    dict((node, None) for node in exampleGraph1), 
    dict((node, False) for node in exampleGraph1)))

print('\nPostorder DFS on example 1:')
postorderVisits = dict((node, None) for node in exampleGraph1)
postorder(exampleGraph1, 'u', 
    dict((node, None) for node in exampleGraph1), 
    dict((node, False) for node in exampleGraph1),
    postorderVisits, [1])
print(postorderVisits)

print('\nPreorder DFS on example 1:')
preorderVisits = dict((node, None) for node in exampleGraph1)
preorder(exampleGraph1, 'u', 
    dict((node, None) for node in exampleGraph1), 
    dict((node, False) for node in exampleGraph1),
    preorderVisits, [1])
print(preorderVisits)

exampleGraph2 = defaultdict(set)
exampleGraph2['a'] = {'b'}
exampleGraph2['b'] = {'c', 'e', 'f'}
exampleGraph2['c'] = {'d', 'g'}
exampleGraph2['d'] = {'c', 'h'}
exampleGraph2['e'] = {'a', 'f'}
exampleGraph2['f'] = {'g'}
exampleGraph2['g'] = {'f'}
exampleGraph2['h'] = {'g'}

print('\nRegular DFS on example 2:')
print(DFS(exampleGraph2, 'a', 
    dict((node, None) for node in exampleGraph2), 
    dict((node, False) for node in exampleGraph2)))

print('\nPostorder DFS on example 2:')
postorderVisits = dict((node, None) for node in exampleGraph2)
postorder(exampleGraph2, 'a', 
    dict((node, None) for node in exampleGraph2), 
    dict((node, False) for node in exampleGraph2),
    postorderVisits, [1])
print(postorderVisits)

print('\nPreorder DFS on example 2:')
preorderVisits = dict((node, None) for node in exampleGraph2)
preorder(exampleGraph2, 'a', 
    dict((node, None) for node in exampleGraph2), 
    dict((node, False) for node in exampleGraph2),
    preorderVisits, [1])
print(preorderVisits)