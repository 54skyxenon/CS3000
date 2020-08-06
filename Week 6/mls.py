#!/usr/local/bin/python3
# Author: Brandon Liang

# MLS - Minimum Lateness Scheduling
# Given a list of jobs and their deadlines, output a minimum lateness schedule for the jobs


def mls(jobs):
    return [job[2] for job in sorted(jobs, key=lambda x: x[1])]


# job length, job deadline, job number
jobs1 = [[1, 2, 1], [2, 4, 2], [3, 6, 3]]
jobs2 = [[1, 20, 1], [10, 10, 2]]
jobs3 = [[1, 2, 1], [10, 10, 2]]
assert mls(jobs1) == [1, 2, 3]
assert mls(jobs2) == [2, 1]
assert mls(jobs3) == [1, 2]
