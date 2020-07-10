#!/usr/local/bin/python3
# Author: Brandon Liang

# WIS - weighted interval scheduling

# The farthest interval such that the finish time is before the start 
# time of the ith interval
def p(i):
    if i == 0:
        return 0

    start_i = v[i - 1][0]
    p_i = 0

    for start, finish, _ in v:
        if finish <= start_i:
            p_i += 1
        
    return p_i

# Naive recursive solution to find *value* of optimal schedule
def FindOPT(n):
    if n == 0:
        return 0
    elif n == 1:
        return v[n - 1][2]
    else:
        return max(FindOPT(n - 1), v[n - 1][2] + FindOPT(p(n)))

# Bottom-up DP solution to do the above, returning the DP table as welll
def efficientFindOPT(n):
    dp = [0 for _ in range(n + 1)]
    pValues = [p(i) for i in range(n + 1)]

    if len(dp) > 1:
        dp[1] = v[0][2]
        
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], v[i - 1][2] + dp[pValues[i]])
    
    return dp

# Find the optimal schedule given the optimal values
def FindSched(dp, n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif v[n - 1][2] + dp[p(n)] > dp[n - 1]:
        return [n] + FindSched(dp, p(n))
    else:
        return FindSched(dp, n - 1)
    
# Each cell consists of (starting, ending, value)
v = [(1, 5, 2), (2, 7, 4), (6, 8, 4), (3, 11, 7), (9, 12, 2), (10, 13, 1)]

assert FindOPT(6) == efficientFindOPT(6)[-1] == 8
assert FindSched(efficientFindOPT(6), 6) == [5, 3, 1]

# Example in class
v = [(0, 2, 3), (4, 5, 5), (1, 7, 9), (6, 10, 6), (4.5, 12, 13), (11, 15, 3)]
print(efficientFindOPT(6))
print(FindSched(efficientFindOPT(6), 6))