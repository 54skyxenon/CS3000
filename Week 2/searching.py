#!/usr/local/bin/python3
# Author: Brandon Liang

# Returns index of target in nums
# If the target doesn't exist, return -1
def binarySearch(nums, target):
    def bsHelper(nums, target, lo, hi):
        if hi < lo:
            return -1

        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return bsHelper(nums, target, lo, mid - 1)
        else: # nums[mid] < target
            return bsHelper(nums, target, mid + 1, hi)

    return bsHelper(nums, target, 0, len(nums) - 1)

# The dumb way of searching
def linearSearch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1

assert binarySearch([2, 3, 8, 11, 15, 17, 28, 42], 28) == 6
assert binarySearch([2, 3, 8, 11, 15, 17, 28, 42], 3) == 1
assert binarySearch([2, 3, 8, 11, 15, 17, 28, 42], 69) == -1
assert binarySearch([2, 3], 3) == 1
assert binarySearch([2, 3, 6], 2) == 0
assert binarySearch([2, 3], 20) == -1