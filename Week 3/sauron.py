#!/usr/local/bin/python3
# Author: Brandon Liang

# Takes O(n) time to build DP table
def sauronDPTable(epochs):
    dp = [0 for _ in epochs]
    dp[0] = max(epochs[0:1])
    dp[1] = max(epochs[0:2])
    dp[2] = max(epochs[0:3])
    dp[3] = max(epochs[0:4])

    for i in range(4, len(epochs)):
        dp[i] = max(dp[i - 1], epochs[i] + dp[i - 4])

    return dp

# Takes O(n) time to build the solution from the DP table
def sauron(epochs):
    if len(epochs) < 5:
        return [epochs.index(max(epochs)) + 1]

    def findSolution(dp, n):
        if n < 0:
            return []
        elif n == 0:
            return [1]
        elif dp[n - 1] != dp[n]:
            return [n + 1] + findSolution(dp, n - 4)
        else:
            return findSolution(dp, n - 1)

    dp = sauronDPTable(epochs)

    print('the epochs: {0}'.format(str(epochs)))
    print('the dp table: {0}'.format(dp))
    # sorting isn't necessary but nice, assume this isn't factored in the overall runtime
    return sorted(findSolution(dp, len(epochs) - 1))

print('the optimal solution: {0}\n'.format(sauron([1, 7, 8, 2, 6, 3])))