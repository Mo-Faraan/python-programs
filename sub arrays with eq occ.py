""" Sub-arrays with equal number of occurences
Difficulty: HardAccuracy: 51.6%Submissions: 3K+Points: 8
Given an array arr[] and two integers say, x and y, find the number of sub-arrays in which the number of occurrences of x is equal to the number of occurrences of y.

Examples:

Input: arr[] = [1, 2, 1] , x= 1 , y = 2
Output: 2
Explanation: The possible sub-arrays have same equal number of occurrences of x and y are:
1) [1, 2], x and y have same occurrence(1).
2) [2, 1], x and y have same occurrence(1).
Input: arr[] = [1, 2, 1] , x = 4 , y = 6
Output: 6
Explanation: The possible sub-arrays have same equal number of occurrences of x and y are:
1) [1], x and y have same occurrence(0).
2) [2], x and y have same occurrence(0).
3) [1], x and y have same occurrence(0).
4) [1, 2], x and y have same occurrence(0).
5) [2, 1], x and y have same occurrence(0).
6) [1, 2, 1], x and y have same occurrence(0). """

class Solution:
    def sameOccurrence(self, arr, x, y):
        count = 0
        prefsum =0
        freqmap = {0:1}
        
        for num in arr:
            if num==x:
                prefsum+=1
            if num ==y:
                prefsum-=1
            if prefsum in freqmap:
                count+=freqmap[prefsum]
                freqmap[prefsum]+=1
            else:
                freqmap[prefsum]=1
        print(freqmap)
        return count
