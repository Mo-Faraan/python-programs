# 242. Valid Anagram

**Difficulty:** Easy

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

---

### Example 1

**Input:**  
`s = "anagram"`, `t = "nagaram"`

**Output:**  
`true`

### Example 2

**Input:**  
`s = "rat"`, `t = "car"`

**Output:**  
`false`

---

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

## Solution

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        Map<Character, Integer> freq = new HashMap<>();
        Map<Character, Integer> freq2 = new HashMap<>();
        for (char i : s.toCharArray()){
            if (freq.containsKey(i)){
                freq.put(i, freq.get(i)+1);
            }
            else{
                freq.put(i, 1);
            }
        }
        for (char i : t.toCharArray()){
            if (freq2.containsKey(i)){
                freq2.put(i, freq2.get(i)+1);
            }
            else{
                freq2.put(i, 1);
            }
        }
        if (freq.equals(freq2)) return true;
        return false;
    }
}
```