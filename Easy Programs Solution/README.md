# Easy Program Solutions
## Easy 1
<p><strong>Question:</strong></p>
<p>Given a string <code>s</code> consisting of words and spaces, return the length of the last word in the string.
A word is a maximal 
substring consisting of non-space characters only.</p>
<p><strong>Solution:</strong></p>
<!-- tabs:start -->

#### **Python3**

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = s.strip()
        strList = stripped.split(" ")
        lastWord = strList[-1]
        return len(lastWord)
#Example usage
txt = "Hello World"
solution = Solution()
result = solution.lengthOfLastWord(txt)
print(result)
```
<p><strong>Explanation of the code:</strong></p>
<p>
This code implements a simple algorithm for finding the length of the last word in a string:

**Step 1: Removing Whitespaces using strip()**

* `s.strip()` removes leading and trailing whitespace from the `s` string. This ensures we only consider the actual words and not any surrounding spaces.

**Step 2: Splitting String into Words using split()**

* `stripped.split(" ")` splits the string `stripped` into a list of words (`strList`) using space as the delimiter.

**Step 3: Extracting the Last Word**

* `strList[-1]` accesses the last element of the list `strList`, which is the last word in the original string.

**Step 4: Calculating the Length of the last word**

* `len(lastWord)` returns the length of the last word stored in the variable `lastWord`.

**Overall Complexity:**

* Time Complexity: O(n) where n is the length of the string. This is due to the string operations involved.
* Space Complexity: O(n) due to the creation of the `strList` which stores the individual words.

**Example Usage Output:**
```
txt = "Hello World"
output = 5
```

</p>

