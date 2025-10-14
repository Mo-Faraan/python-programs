# Top K Frequent Elements

**Solved**

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

---

## Example 1

**Input:**  
`nums = [1,2,2,3,3,3]`, `k = 2`

**Output:**  
`[2,3]`

---

## Example 2

**Input:**  
`nums = [7,7]`, `k = 1`

**Output:**  
`[7]`

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`
- `1 <= k <= number of distinct elements in nums`

---

## Solution

```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencyBucket = [[] for i in range(len(nums)+1)]
        freqMap = {}
        res = []
        for i in nums:
            freqMap[i] = 1 + freqMap.get(i, 0)
        for (num, freq) in freqMap.items():
            frequencyBucket[freq].append(num)
        for i in range(len(frequencyBucket)-1, 0, -1):
            if frequencyBucket[i] != []:
                for j in frequencyBucket[i]:
                    res.append(j)
                    if len(res) == k :
                        return res


# 0  1  2  3   4  5  6      // Bucket Sort
# [] [] [x,y] [] [z] [] []

```

```
public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];

        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int index = 0;
        for (int i = freq.length - 1; i > 0 && index < k; i--) {
            for (int n : freq[i]) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }
        return res;
    }
}

```