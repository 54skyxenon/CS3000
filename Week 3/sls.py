#!/usr/local/bin/python3

# SLS - segmented least squares allows us to describe data in terms of multiple 
# linear fits
import numpy as np
import warnings

warnings.filterwarnings("ignore", message="Polyfit may be poorly conditioned")

# do preprocessing to obtain error terms - O(n^2)
def getEpsilons():
    def error(i, j):
        selectedPoints = points[i:j+1]

        xs = np.array([point[0] for point in selectedPoints])
        ys = np.array([point[1] for point in selectedPoints])

        a, b = 0, ys[0] 

        if len(selectedPoints) > 1:
            a, b = np.polyfit(xs, ys, 1).round(decimals=5)
        
        return sum([(point[1] - (a * point[0]) - b) ** 2 for point in selectedPoints])

    epsilons = np.zeros((len(points), len(points)))
    for i in range(len(points)):
        for j in range(i, len(points)):
            epsilons[i][j] = error(i, j)
    
    return epsilons

# fill the DP table and return both DP and epsilon tables - O(n)
def fillTables(n):
    dp = [0 for _ in range(n + 1)]
    dp[1] = cost
    dp[2] = cost
    epsilons = getEpsilons()

    for j in range(3, n + 1):
        dp[j] = min([(epsilons[i - 1][j - 1] + cost + dp[i - 1]) for i in range(1, j + 1)])
    
    return dp, epsilons

# find the optimum solution given DP table and epsilons - O(n^2)
def sls(n):
    dp, epsilons = fillTables(n)

    def findSolution(dp, n):
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        else:
            argmin = [(epsilons[i - 1][n - 1] + cost + dp[i - 1]) for i in range(1, n + 1)]
            x = argmin.index(min(argmin)) + 1
            return [list(range(x, n + 1))] + findSolution(dp, x - 1)

    return findSolution(dp, n)

# fill the DP table for V2 and return both DP and epsilon tables - O(n)
def fillTablesV2(n, k):
    dp = np.zeros((n + 1, k + 1))
    dp[1:,0] = float('inf') 
    epsilons = getEpsilons()

    for l in range(1, k + 1):
        for j in range(1, n + 1):
            dp[j][l] = min([epsilons[i - 1][j - 1] + dp[i - 1][l - 1] for i in range(1, j + 1)])

    return dp, epsilons

# sls, but instead of a cost, we're given a max number of lines to use (k)
def slsV2(n, k):
    if k == 1:
        return [list(range(1, n + 1))]
    
    dp, epsilons = fillTablesV2(n, k)

    def findSolution(dp, n, k):
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        else:
            argmin = [(epsilons[i - 1][n - 1] + dp[i - 1][k - 1]) for i in range(1, n + 1)]
            x = argmin.index(min(argmin)) + 1
            return [list(range(x, n + 1))] + findSolution(dp, x - 1, k - 1)

    return findSolution(dp, n, k)

# global vars
points = [(1, 1), (2, 1), (3, 3)]
print('\nVersion 1:')

# cost is small enough to break into two
cost = 0.2
print(sls(len(points)))

# cost is too great to break into two
cost = 2
print(sls(len(points)))

print('\nVersion 2:')
# better example for version 2 (restricted to 1-4 lines)
points = [(1, 1), (2, 1), (3, 3), (5, 5), (6, 5), (7, 5)]
print(slsV2(len(points), 1))
print(slsV2(len(points), 2))
print(slsV2(len(points), 3))
print(slsV2(len(points), 4))