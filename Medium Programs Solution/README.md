# MediumProgram Solutions
## Medium 2
<p><strong>Question:</strong></p>
<p>Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.</p>
<p><strong>Solution:</strong></p>
<!-- tabs:start -->

#### **Python3**

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Create a Counter to store the count of each element
        element_count = Counter(nums)
        
        majority_elements = []
        threshold = len(nums) // 3
               
        for element, count in element_count.items():
            
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements
 
 #Example Usage       
nums = [3, 2, 3]
solution = Solution()
result =  solution.majorityElement(nums)
print(result)

```
**Example Usage Output:**
```
Input: nums = [3,2,3]
Output: [3]
```

<p><strong>Explanation of the code:</strong></p>
<p>
## Logic and Algorithm Explanation for `majorityElement`

This code implements Boyer-Moore voting algorithm to find all elements that appear more than `n/3` times in a given list.

**Step 1: Count Elements**

* `Counter(nums)` creates a dictionary `element_count` where keys are unique elements in `nums` and values are their corresponding frequencies.

**Step 2: Initialize Variables**

* `majority_elements` is an empty list to store the identified majority elements.
* `threshold` is calculated as the floor division of the total elements `len(nums)` by 3. This represents the minimum count required for an element to be considered a majority element.

**Step 3: Loop through Element Counts**

* A loop iterates through each element and its count stored in `element_count`.

**Step 4: Check for Majority**

* The `if` statement compares the current element's count (`count`) with the threshold.
    * If `count > threshold`, it implies the current element appears more than `n/3` times.
    * In such cases, the element is appended to the `majority_elements` list.

**Step 5: Return Results**

* After iterating through all elements, the `majority_elements` list contains all elements that satisfied the majority criteria.
* The function returns `majority_elements`.

**Algorithm Logic:**

1. Count the occurrences of each element in the list.
2. Set a threshold as the floor division of the list length by 3.
3. Check if any element's count exceeds the threshold.
4. If an element's count is greater than the threshold, it appears more than `n/3` times and is considered a majority element.
5. Add the identified majority elements to a list and return it.

**Complexity:**

* Time Complexity: O(n)
    * The loop iterates through all elements once, leading to linear time complexity.
* Space Complexity: O(n)
    * The `Counter` object and `majority_elements` list require space proportional to the number of distinct elements.

</p>

## Medium 3
<p><strong>Question:</strong></p>
<p>
  
* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 300
* matrix[i][j] is '0' or '1'.

<code><pre>*Example 2:*
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4</pre></code>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg" style="width: 400px; height: 319px;" />
</p>

<p><strong>Solution:</strong></p>
<!-- tabs:start -->

#### **Python3**

```python
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        a, b = len(matrix), len(matrix[0])
        d = [[0] * (b + 1) for _ in range(a + 1)]
        m = 0
        for i in range(a):
            for j in range(b):
                if matrix[i][j] == '1':
                    d[i + 1][j + 1] = min(d[i][j + 1], d[i + 1][j], d[i][j]) + 1
                    m = max(m, d[i + 1][j + 1])
        return m * m
#Example Usage
matrix = [["0","1"],["1","0"]]
solution = Solution()
result = solution.maximalSquare(matrix)
print(result)

```
**Example Usage Output:**
```
matrix = [["0","1"],["1","0"]]
output = 1
```
<p><strong>Explanation of the code:</strong></p>
<p>
  ## Logic and Algorithm for `maximalSquare`

This code implements a dynamic programming algorithm to find the largest square submatrix with all "1"s in a binary matrix.

**Step 1: Initialize Variables**

* `a`: Stores the number of rows in the matrix (`len(matrix)`)
* `b`: Stores the number of columns in the matrix (`len(matrix[0])`)
* `d`: Creates a 2D array of size (a+1) x (b+1) to store side lengths of squares
* `m`: Initializes a variable to track the maximum side length

**Step 2: Loop through Rows and Columns**

* A nested loop iterates through each cell in the matrix.
* `i`: Represents the row index (0 to a-1)
* `j`: Represents the column index (0 to b-1)

**Step 3: Check Current Cell**

* The `if` statement checks if the current cell (`matrix[i][j]`) contains "1".

**Step 4: Calculate Square Side Length**

* If the current cell is "1", the side length of the square ending at this cell is calculated as:
    * Minimum of:
        * Side length of the square ending at the cell above (`d[i][j + 1]`)
        * Side length of the square ending at the cell to the left (`d[i + 1][j]`)
        * Side length of the square ending at the diagonal cell above and left (`d[i][j]`)
    * Add 1 to account for the current cell itself

**Step 5: Update Matrix and Maximum Side Length**

* The calculated side length (`d[i + 1][j + 1]`) is stored in the corresponding position of the `d` matrix.
* The `m` variable is updated with the maximum side length encountered so far by comparing it with the newly calculated side length.

**Step 6: Return Result**

* After iterating through all cells, the `m` variable holds the side length of the largest square with all "1"s.
* The function returns the square area (`m * m`).

**Algorithm Logic:**

1. Build a 2D array to store side lengths of squares ending at each cell.
2. Start from the bottom left corner and iterate through each cell.
3. If the current cell is "1", calculate its side length based on neighboring cells.
4. Update the side length matrix and track the maximum side length encountered.
5. Finally, return the area of the square with the maximum side length.

**Complexity:**

* Time Complexity: O(m * n)
    * The nested loop iterates through each cell in the matrix, leading to linear time complexity based on matrix size.
* Space Complexity: O(m * n)
    * The `d` matrix requires space proportional to the matrix size.
</p>



