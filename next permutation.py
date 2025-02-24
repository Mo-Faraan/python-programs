'''Next Permutation
Last Updated : 17 Feb, 2025
Given an array arr[] of size n, the task is to print the lexicographically 
next greater permutation of the given array. If there does not exist any greater 
permutation, then find the lexicographically smallest permutation of the given array.

Let us understand the problem better by writing all permutations of [1, 2, 4] in 
lexicographical order: [1, 2, 4], [1, 4, 2], [2, 1, 4], [2, 4, 1], [4, 1, 2] and [4, 2, 1]. 
If we give any of the above (except the last) as input, we need to find the next one in sequence. 
If we give last as input, we need to return the first one.'''

def nextper(arr):
    n= len(arr)
    pivot = -1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            pivot = i
            break
    if pivot == -1:
        arr.reverse()
        return arr
    for i in range(n-1,pivot,-1):
        if arr[i]>arr[pivot]:
            arr[i],arr[pivot]=arr[pivot],arr[i]
            break
    left = pivot+1
    right = n-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

arr = list(map(int,input().split()))
print(" ".join(map(str,nextper(arr))))