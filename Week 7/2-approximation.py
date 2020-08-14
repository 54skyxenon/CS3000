#!/usr/local/bin/python3
# Author: Brandon Liang

import random

# Approximation algorithms sacrifice accuracy for a better runtime
# We can use a 2-approximation for the MVC problem to guarantee that our answer is at most twice of the optimal one

# First approach (simple)
def mvcApprox1(graph):
    # Pick an edge in graph and add both endpoints to cover
    def pickEdge():
        for u in graph:
            for v in graph[u]:
                return (u, v)

    # Delete edges incident to endpoints from graph
    def deleteEdge(u, v):
        for node in graph:
            if node == u or node == v:
                graph[node] = set()
            else:
                graph[node] -= {u, v}

    cover = set()
    while pickEdge():
        e = pickEdge()
        cover.add(e[0])
        cover.add(e[1])
        deleteEdge(*e)
    
    return cover

# Second approach (DFS)
def mvcApprox2(graph):
    cover = set()
    start = random.sample(graph.keys(), 1)[0]
    visited = {start}

    def DFS(curr):
        for neighbor in (graph[curr] - visited):
            cover.add(curr)
            visited.add(neighbor)
            DFS(neighbor)
    
    DFS(start)
    return cover

def getExample1():
    graphExample1 = dict()
    graphExample1[1] = {2, 3, 4}
    graphExample1[2] = {1}
    graphExample1[3] = {1}
    graphExample1[4] = {1}

    return graphExample1

def getExample2():
    graphExample2 = dict()
    graphExample2[1] = {2, 3, 5, 6}
    graphExample2[2] = {1}
    graphExample2[3] = {1, 5}
    graphExample2[4] = {6, 7}
    graphExample2[5] = {1, 3, 7, 8}
    graphExample2[6] = {1, 4}
    graphExample2[7] = {4, 5}
    graphExample2[8] = {5}

    return graphExample2

print(mvcApprox1(getExample1()))
print(mvcApprox1(getExample2()))
print(mvcApprox2(getExample1()))
print(mvcApprox2(getExample2()))