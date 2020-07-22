#!/usr/local/bin/python3
# Author: Brandon Liang

from collections import deque, defaultdict

# O(n^2 + nm) algorithm for topological ordering a DAG
def simpleTopOrder(graph):
    i = 1
    labeled = dict()

    incomingEdges = defaultdict(int)
    for node in graph:
        for outneighbor in graph[node]:
            incomingEdges[outneighbor] += 1

    while graph:
        # Find a node u with no incoming edges
        u = None
        for node in graph:
            if incomingEdges[node] == 0:
                u = node
                break

        # Label u as node i, increment i by 1
        labeled[u] = i
        i += 1

        # Remove u and its edges from G
        for outneighbor in graph[u]:
            incomingEdges[outneighbor] -= 1

        del graph[u]

    return labeled

# O(n + m) algorithm for topological ordering a DAG
def fastTopOrder(graph):
    i = 1
    labeled = dict()

    # Mark all nodes with their # of in-edges
    incomingEdges = defaultdict(int)
    for node in graph:
        for outneighbor in graph[node]:
            incomingEdges[outneighbor] += 1

    # Put all nodes w/ mark 0 in queue Q
    q = deque()
    for node in graph:
        if incomingEdges[node] == 0:
            q.append(node)

    def deleteNode(v):
        nonlocal i
        # Label v as node i in the top. order
        labeled[v] = i
        i = i + 1

        for w in graph[v]:
            # Decrease w’s mark by 1
            incomingEdges[w] -= 1
        
        for w in graph[v]:
            if incomingEdges[w] == 0:
                deleteNode(w)
    
    while q:
        u = q.popleft()
        deleteNode(u)

    return labeled

graphExample = dict()
graphExample['v1'] = {'v4', 'v5', 'v7'}
graphExample['v2'] = {'v3', 'v5', 'v6'}
graphExample['v3'] = {'v4', 'v5'}
graphExample['v4'] = {'v5'}
graphExample['v5'] = {'v6', 'v7'}
graphExample['v6'] = {'v7'}
graphExample['v7'] = set()
print(simpleTopOrder(graphExample))

graphExample = dict()
graphExample['v1'] = {'v4', 'v5', 'v7'}
graphExample['v2'] = {'v3', 'v5', 'v6'}
graphExample['v3'] = {'v4', 'v5'}
graphExample['v4'] = {'v5'}
graphExample['v5'] = {'v6', 'v7'}
graphExample['v6'] = {'v7'}
graphExample['v7'] = set()
print(fastTopOrder(graphExample))

