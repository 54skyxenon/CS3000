#!/usr/local/bin/python3
# Author: Brandon Liang

# All functions return copies and avoid mutation
def selectionSort(arr):
    arr = arr[:]
    for i in range(len(arr) - 1):
        maxIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[maxIndex]:
                maxIndex = j

        tmp = arr[i]
        arr[i] = arr[maxIndex]
        arr[maxIndex] = tmp

    return arr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    first = mergeSort(arr[:len(arr)//2])
    second = mergeSort(arr[len(arr)//2:])

    def merge(arr1, arr2):
        index1 = 0
        index2 = 0

        newArr = []

        while index1 + index2 < len(arr1) + len(arr2):
            if index1 == len(arr1):
                newArr.append(arr2[index2])
                index2 += 1
            elif index2 == len(arr2):
                newArr.append(arr1[index1])
                index1 += 1
            elif arr1[index1] < arr2[index2]:
                newArr.append(arr1[index1])
                index1 += 1
            else:
                newArr.append(arr2[index2])
                index2 += 1
        
        return newArr

    return merge(first, second)

example1 = [11, 3, 42, 28, 17, 8, 2, 15]
print(sorted(example1))
assert selectionSort(example1) == mergeSort(example1) == sorted(example1)