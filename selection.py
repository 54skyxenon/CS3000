#!/usr/local/bin/python3
# Author: Brandon Liang

import math
import random

# Retrieve the minimum element from the list => O(n)
def getMinItem(nums):
    if not nums:
        raise ValueError('List must have at least one element!')

    minItem = float('inf')
    for i in range(len(nums)):
        minItem = min(minItem, nums[i])

    return minItem

# Retrieve the second minimum item from the list => O(n)
def getSecondMinItem(nums):
    if len(nums) < 2:
        raise ValueError('List must have at least two elements!')

    indexOfMin = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[indexOfMin]:
            indexOfMin = i

    secondMinItem = float('inf')
    for i in range(1, len(nums)):
        if i == indexOfMin:
            continue
        else:
            secondMinItem = min(nums[i], secondMinItem)

    return secondMinItem

# Retrieve the kth minimum item from the list => O(n log n)
def getKthMinItem(nums, k):
    if k > len(nums):
        raise ValueError('Not enough items in list!')

    return sorted(nums)[k - 1]

# Retrieve median element from list => O(n log n)
def getMedianItem(nums):
    if not nums:
        raise ValueError('List must have at least one element!')

    return getKthMinItem(nums, len(nums) // 2)

# Retrieve kth minimum item from list efficiently => O(n)
def quickselect(nums, k):
    def partition(pivotIndex, nums):
        nums[pivotIndex], nums[0] = nums[0], nums[pivotIndex]
        pivot = nums[0]

        lo = 1
        for index in range(1, len(nums)):
            if nums[index] < pivot:
                nums[index], nums[lo] = nums[lo], nums[index]
                lo += 1
            
        nums[0], nums[lo - 1] = nums[lo - 1], nums[0]
        return lo - 1

    if len(nums) == 1:
        return nums[0]

    r = partition(0, nums) + 1

    if k == r:
        return nums[r - 1]
    elif k < r:
        return quickselect(nums[:r-1], k)
    elif k > r:
        return quickselect(nums[r:], k - r)


example = [11, 3, 42, 28, 17, 8, 2, 15]

assert getMinItem(example) == 2
assert getSecondMinItem(example) == 3
assert getKthMinItem(example, 6) == 17
assert getMedianItem(example) == 11

# Stress test
for i in range(2, 101):
    testCase = [random.randint(-1000, 1000) for _ in range(i)]
    kthOrderStatistic = random.choice(range(len(testCase))) + 1
    assert getKthMinItem(testCase, kthOrderStatistic) == quickselect(testCase, kthOrderStatistic)