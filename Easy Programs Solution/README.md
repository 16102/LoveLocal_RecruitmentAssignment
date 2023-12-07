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

## Easy 3
<p><strong>Question:</strong></p>
<p>Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="width: 400px; height: 319px;" />
<p><strong>Solution:</strong></p>
<!-- tabs:start -->

#### **Python3**

```python
class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev = triangle[-1]
            current = [1]
            
            for j in range(1, i):
                current.append(prev[j - 1] + prev[j])
            
            current.append(1)
            triangle.append(current)
        
        return triangle

# Example usage:
numRows = 5
solution=Solution()
result= solution.generate(numRows)
print("NumRows = ",numRows)
print(result)

```
<p><strong>Explanation of the code:</strong></p>
<p>
This code implements Pascal's triangle algorithm to generate a list containing the first n rows of the triangle.

**Step 1: Base Case**

* If `numRows` is 0, an empty list is returned. This is because Pascal's triangle has no rows when n is 0.

**Step 2: Initialize Triangle**

* A list called `triangle` is initialized with a single element list containing 1. This represents the first row of the triangle.

**Step 3: Loop through Rows**

* A loop iterates from 1 to `numRows` (excluding 0), generating each row of the triangle.

**Step 4: Generate Current Row**

* A variable `prev` stores the previous row of the triangle.
* An empty list called `current` is created to store the elements of the current row.
* A single 1 (representing the first element of every row) is added to `current`.

**Step 5: Calculate Inner Elements**

* A nested loop iterates from 1 to the current row number (excluding 0).
* Inside the loop, the value at the current index of the current row is calculated as the sum of the element at the same index and the element one position to the right in the previous row. This is the core logic of Pascal's triangle.
* The calculated value is appended to the `current` list.

**Step 6: Add Last Element**

* Another 1 is added to the `current` list, representing the last element of the row.

**Step 7: Update Triangle**

* The `current` list is appended to the `triangle` list, effectively adding the newly generated row to the overall triangle.

**Step 8: Return Result**

* After all rows are generated, the `triangle` list containing the entire Pascal's triangle for the specified number of rows is returned.

**Complexity:**

* Time Complexity: O(n^2). This is due to the nested loop iterating through each element of the triangle.
* Space Complexity: O(n^2). This is due to the storage of the entire Pascal's triangle in the `triangle` list.

**Example Usage Output:**
```
NumRows =  5
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

</p>

