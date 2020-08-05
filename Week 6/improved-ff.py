#!/usr/local/bin/python3
# Author: Brandon Liang

from collections import defaultdict

def fordFulkerson(network):
    residual = defaultdict(dict)
    for u in network:
        for v in network[u]:
            residual[u][v] = network[u][v]
            residual[v][u] = 0

    # DIFFERENCE: We'll select a smart augmented path this time
    def findAugmentingPath(curr, acc, visited):
        pass

    maxFlow = float('-inf')
    while True:
        augmentingPath = findAugmentingPath('s', ['s'], {'s'})

        if not augmentingPath:
            return maxFlow

        augment = float('inf')
        for i in range(len(augmentingPath) - 1):
            first = augmentingPath[i]
            second = augmentingPath[i + 1]
            augment = min(augment, residual[first][second])

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


