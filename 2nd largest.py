'''
Second Largest Element in an Array
Last Updated : 10 Feb, 2025
Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

Note: If the second largest element does not exist, return -1.'''
def seclar(arr):
    n = len(arr)
    largest = -1
    seclarg = -1
    for i in range(n):
        if arr[i]>largest :
            seclarg = largest
            largest = arr[i]
        elif arr[i]>seclarg and arr[i]<largest:
            seclarg = arr[i]
    return seclarg
arr = list(map(int,input().split()))
print(seclar(arr))