#!/usr/local/bin/python3
# Author: Brandon Liang

from collections import defaultdict

# Dijkstra's single-source shortest path algorithm
def dijkstra(graph, start):
    explored = {start}
    unexplored = graph.keys() - {start}

    dists = dict((node, float('inf')) for node in graph)
    dists[start] = 0

    def fillDists(current, acc):
        # TODO: finish tmrw
        pass
        
    fillDists(start, 0)
    return dists

graphExample1 = defaultdict(dict)
graphExample1['A'] = {'B': 10, 'C': 3}
graphExample1['B'] = {'C': 1, 'D': 2}
graphExample1['C'] = {'B': 4, 'D': 8, 'E': 2}
graphExample1['D'] = {'E': 7}
graphExample1['E'] = {'D': 9}

dijkstra(graphExample1, 'A')