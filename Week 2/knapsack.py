#!/usr/local/bin/python3
# Author: Brandon Liang

import numpy as np

# (weight, value)
items = [(2, 4), (3, 5), (5, 8)]

# Get the DP table of optimum values for each item, weight pair
def knapsackDPTable(T, n):
    dp = np.zeros((n + 1, T + 1), dtype=int)

    # item index
    for j in range(1, n + 1):
        # weight index
        for S in range(1, T + 1):
            if S < items[j - 1][0]:
                dp[j][S] = dp[j - 1][S]
            else:
                dp[j][S] = max(dp[j - 1][S], items[j - 1][1] + dp[j - 1][S - items[j - 1][0]])

    return dp

# Use DP table to find optimal subset, fully answering the original question
def knapsack(dp, T, n):
    if n == 0 or T == 0:
        return []
    elif items[n - 1][0] > T:
        return knapsack(dp, T, n - 1)
    elif dp[n - 1][T] > (items[n - 1][1] + dp[n - 1][T - items[n - 1][0]]):
        return knapsack(dp, T, n - 1)
    else:
        return [n] + knapsack(dp, T - items[n - 1][0], n - 1)

table = knapsackDPTable(8, 3)
print(table)
print(knapsack(table, 8, 3))
