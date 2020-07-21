#!/usr/local/bin/python3
# Author: Brandon Liang

from collections import deque, defaultdict
import random

# NOTE: this is same solution I gave for https://leetcode.com/problems/is-graph-bipartite/
# Except I change the graph argument to be a dictionary mapping to sets
# And graph nodes don't necessarily have to conform to indices

''' Uses BFS to determine if a graph is bipartite - "a graph is bipartite if we can split 
it's set of nodes into two independent subsets A and B such that every edge in the graph 
has one node in A and another node in B." '''

def isBipartite(graph):
    if not graph:
        return True
    
    # Necessary in case graph isn't connected
    unvisited = graph.keys()
    def BFS(graph, start):
        purple, red = set(), set()
        seen = {start}
        
        q = deque()
        q.append((start, 0))
        
        while q:
            currNode, currLayer = q.popleft()
            if currLayer % 2 == 0:
                purple |= {currNode}
            else:
                red |= {currNode}
            
            for neighbor in graph[currNode]:
                if neighbor not in seen:
                    seen |= {neighbor}
                    q.append((neighbor, currLayer + 1))
            
        return purple, red
    
    while unvisited:
        purple, red = BFS(graph, random.sample(unvisited, 1)[0])
        unvisited -= purple
        unvisited -= red
        
        allPurplesPointToRed = all(graph[pNode].issubset(red) for pNode in purple)
        allRedsPointToPurple = all(graph[rNode].issubset(purple) for rNode in red)
        
        if not allPurplesPointToRed or not allRedsPointToPurple:
            return False
        
    return True

yesBipartite = defaultdict(set)
yesBipartite[1] = {2, 3, 5}
yesBipartite[2] = {1}
yesBipartite[3] = {1, 4}
yesBipartite[4] = {3, 5}
yesBipartite[5] = {1, 4}

noBipartite = defaultdict(set)
noBipartite[1] = {2, 3}
noBipartite[2] = {1, 3, 5, 4}
noBipartite[3] = {1, 7, 8, 5, 2}
noBipartite[4] = {2, 5}
noBipartite[5] = {6, 4, 2, 3}
noBipartite[6] = {5}
noBipartite[7] = {3, 8}
noBipartite[8] = {3, 7}

assert isBipartite(yesBipartite)
assert not isBipartite(noBipartite)