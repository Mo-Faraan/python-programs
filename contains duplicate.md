# 217. Contains Duplicate

**Difficulty:** Easy  
**Topics:** Array, Hash Table  
**Companies:** [Premium lock icon]

---

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

## Examples

### Example 1

**Input:**  
`nums = [1,2,3,1]`

**Output:**  
`true`

**Explanation:**  
The element `1` occurs at the indices `0` and `3`.

---

### Example 2

**Input:**  
`nums = [1,2,3,4]`

**Output:**  
`false`

**Explanation:**  
All elements are distinct.

---

### Example 3

**Input:**  
`nums = [1,1,1,3,3,4,3,2,4,2]`

**Output:**  
`true`

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Solution

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int i : nums) {
            if (set.contains(i)) {
                return true;
            }
            set.add(i);
        }
        return false;
    }
}
```