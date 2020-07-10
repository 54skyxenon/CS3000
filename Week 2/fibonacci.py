#!/usr/local/bin/python3
# Author: Brandon Liang

# Naive method of calculating nth fibonacci number => O(1.62^n)
def fibI(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibI(n - 1) + fibI(n - 2)

# Dynamic programming solution with memoization (i.e. top-down) => O(n)
def fibII(n):
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    dp[1] = 1

    def fib(n):
        if dp[n] < 0:
            dp[n] = fib(n - 1) + fib(n - 2)
        
        return dp[n]

    return fib(n - 1)

# Dynamic programming solution with iteration (i.e. bottom-up/tabulation) => O(n)
def fibIII(n):
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, len(dp)):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]

assert fibI(10) == fibII(10) == fibIII(10) == 34