'''Third largest element in an array of distinct elements
Last Updated : 17 Feb, 2025
Given an array of n integers, the task is to find the third largest element. All the elements in the array are distinct integers.
'''
def thirdlar(arr):
    n = len(arr)
    first,second,third = -1,-1,-1
    for i in range(n):
        if arr[i]>first:
            third = second
            second = first
            first = arr[i]
        elif arr[i]>second:
            third = second
            second = arr[i]
        elif arr[i]>third:
            third = arr[i]
    return third

arr = list(map(int,input().split()))
print(thirdlar(arr))
