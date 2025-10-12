## Group anagrams

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Example 1

**Input:**  
`strs = ["eat","tea","tan","ate","nat","bat"]`

**Output:**  
`[["bat"],["nat","tan"],["ate","eat","tea"]]`

**Explanation:**  
- There is no string in `strs` that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

### Example 2

**Input:**  
`strs = [""]`

**Output:**  
`[[""]]`

### Example 3

**Input:**  
`strs = ["a"]`

**Output:**  
`[["a"]]`

---

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## Solution
```
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d={}
        d = defaultdict(list)

        def findFreq(s: str) -> tuple():
            count = [0]*26
            for i in s:
                count[ord(i) - ord('a')]+=1
            return tuple(count)

        for i in strs:
            key = findFreq(i)
            # if key not in d :
            #     d[key] = []
            # d[key].append(i)
            d[key].append(i)
        return list(d.values())
```

```
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> hashMap = new HashMap<>();
        
        for (String word : strs) {
            // Sort the characters of the word
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);  // sorted string is key
            
            // Insert word into the correct bucket
            hashMap.putIfAbsent(key, new ArrayList<>());
            hashMap.get(key).add(word);
        }
        
        return new ArrayList<>(hashMap.values());
    }
}
```