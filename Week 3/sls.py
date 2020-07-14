#!/usr/local/bin/python3

# SLS - segmented least squares
import numpy as np
import warnings

warnings.filterwarnings("ignore", message="Polyfit may be poorly conditioned")

# global vars
points = [(1, 1), (2, 1), (3, 3)]
cost = 0.2

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
        if n <= 0:
            return []
        elif n == 1:
            return [[1]]
        else:
            argmin = [(epsilons[i - 1][n - 1] + cost + dp[i - 1]) for i in range(1, n + 1)]
            x = argmin.index(min(argmin)) + 1
            return [list(range(x, n + 1))] + findSolution(dp, x - 1)

    return findSolution(dp, n)

print(sls(len(points)))