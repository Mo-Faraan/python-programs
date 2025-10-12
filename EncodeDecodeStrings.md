# Encode and Decode Strings

**Solved**

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

## Problem Statement

Implement the following functions:

- `encode(strs: List[str]) -> str`: Encodes a list of strings to a single string.
- `decode(s: str) -> List[str]`: Decodes the encoded string back to the original list of strings.

## Examples

### Example 1

**Input:**  
`["neet", "code", "love", "you"]`

**Output:**  
`["neet", "code", "love", "you"]`

### Example 2

**Input:**  
`["we", "say", ":", "yes"]`

**Output:**  
`["we", "say", ":", "yes"]`

## Constraints

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains only UTF-8 characters.

---

## Solution

```
class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs :
            a = len(i)
            s += str(a) + "#" + i
        return s


    def decode(self, s: str) -> List[str]:
        a=""
        l=[]
        i=0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            a = s[j+1 : j+1 + length]
            l.append(a)
            i = j+1 + length
        return l

```

```
public class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for (String s : strs) {
            res.append(s.length()).append('#').append(s);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(str.substring(i, j));
            i = j + 1;
            j = i + length;
            res.add(str.substring(i, j));
            i = j;
        }
        return res;
    }
}
```