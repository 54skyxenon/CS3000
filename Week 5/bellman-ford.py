#!/usr/local/bin/python3
# Author: Brandon Liang

from collections import defaultdict

# Bellman Ford: a single source shortest path algorithm using DP
# In contrast to Dijkstra, we can handle negative weights (that don't induce a negative cycle)

# Runtime asymptotically is O(nm) for both versions, for n nodes and m edges

# Naive implementation of BF using 2D array and iterating completely
def bellmanFordNaive(graph, start):
    parents = dict((v, [None for j in graph]) for v in graph)

    # stores the distances
    dp = dict((v, [float('inf') for j in graph]) for v in graph)
    dp[start] = [0 for j in graph]

    for i in range(1, len(graph)):
        for v in graph:
            dp[v][i] = dp[v][i - 1]
            parents[v][i] = parents[v][i - 1]

            for u in graph:
                if v in graph[u]:
                    if dp[u][i - 1] + graph[u][v] < dp[v][i]:
                        dp[v][i] = dp[u][i - 1] + graph[u][v]
                        parents[v][i] = u

    # we only want the last columns
    dp = dict((node, dp[node][-1]) for node in dp)
    parents = dict((node, parents[node][-1]) for node in parents)

    return dp, parents 

# Optimized implementation of BF
def bellmanFord(graph, start, detectCycle=False):
    dp = dict((v, float('inf')) for v in graph)
    parents = dict((v, None) for v in graph)
    dp[start] = 0
    
    changed = dict((v, True) for v in graph)

    for i in range(len(graph)):
        prev = dict((node, dp[node]) for node in dp)

        for v in graph:
            for u in graph:
                if changed[u] and v in graph[u]:
                    if dp[u] + graph[u][v] < dp[v]:
                        dp[v] = dp[u] + graph[u][v]
                        parents[v] = u

        changed = dict((v, prev[v] != dp[v]) for v in prev)
        anyChanged = any([changed[node] for node in changed])

        # we have to iterate over the whole thing if we want to detect a cycle
        if detectCycle:
            if i == len(graph) - 1:
                print('Negative cycle found!' if anyChanged else 'No negative cycle present')
        elif not anyChanged:
            return dp, parents

    return dp, parents

exampleGraph1 = defaultdict(set)
exampleGraph1['s'] = {'b': -1, 'c': 4}
exampleGraph1['b'] = {'c': 3, 'd': 2, 'e': 2}
exampleGraph1['c'] = {}
exampleGraph1['d'] = {'c': 5, 'b': 1}
exampleGraph1['e'] = {'d': -3}

assert bellmanFordNaive(exampleGraph1, 's') == bellmanFord(exampleGraph1, 's')
print(bellmanFord(exampleGraph1, 's', detectCycle=True))

# Both these graphs have cycles
exampleGraph2 = defaultdict(set)
exampleGraph2['u'] = {'v': -8}
exampleGraph2['v'] = {'x': 2}
exampleGraph2['x'] = {'u': -4}
print(bellmanFord(exampleGraph2, 'u', detectCycle=True))

exampleGraph3 = defaultdict(set)
exampleGraph3['a'] = {'b': -1, 'c': 4}
exampleGraph3['b'] = {'c': 3, 'd': 2, 'e': 2}
exampleGraph3['c'] = {}
exampleGraph3['d'] = {'b': 1, 'c': 5}
exampleGraph3['e'] = {'d': -6}
print(bellmanFord(exampleGraph3, 'a', detectCycle=True))