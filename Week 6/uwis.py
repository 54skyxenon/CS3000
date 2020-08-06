#!/usr/local/bin/python3
# Author: Brandon Liang

# Solve the *unweighted* interval scheduling problem with a greedy algorithm
# Weighted would be with DP

# BTW, this is Leetcode Problem 646


def uwis(schedule):
    schedule.sort(key=lambda x: x[1])
    S = list()

    for s in schedule:
        if not S or S[-1][1] <= s[0]:
            S.append(s)

    return S


schedule0 = []
schedule1 = [[1, 2], [2, 3], [3, 4]]
schedule2 = [[-10, -8], [8, 9], [-5, 0],
             [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]]
schedule3 = [[0, 100], [130, 150], [0, 20], [30, 60], [
    70, 90], [110, 160], [0, 40], [50, 65], [80, 120]]

assert len(uwis(schedule0)) == 0
assert len(uwis(schedule1)) == 3
assert len(uwis(schedule2)) == 5
assert len(uwis(schedule3)) == 4
