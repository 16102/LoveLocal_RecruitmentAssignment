# Hard Program Solutions
## Hard 2
<p><strong>Question:</strong></p>
<p>You are given a string <code>s</code>. You can convert <code>s</code> to a 
palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.</p>
<p><strong>Solution:</strong></p>
<!-- tabs:start -->

#### **Python3**

```python
#Hard Program 2
class Solution:
    def findPalindrome(self, s: str) -> str:
        a = s[::-1]

        for i in range(len(a)):
            if s.startswith(a[i:]):
                return a[:i] + s

        return a + s

#Example Usage
s = "abcd"
solution = Solution()
result = solution.findPalindrome(s)
print(result)
```
**Example Usage Output:**
```
s = "abcd"
output = dcbabcd
```

<p><strong>Explanation of the code:</strong></p>
<p>
This code implements an algorithm to find the longest palindrome within a given string. The key points are:

**Step 1: Reverse the String**

* `a = s[::-1]` creates a reversed copy of the original string `s`. This simplifies the comparison process later.

**Step 2: Iterative Search**

* A loop iterates through each character of the reversed string `a`, starting from the end.

**Step 3: Check for Prefix Match**

* Inside the loop, the `s.startswith(a[i:])` condition checks if the original string `s` starts with the substring of `a` from index `i` onwards. This effectively checks if the current character and all subsequent characters in `a` are present at the beginning of `s`.

**Step 4: Found Palindrome**

* If the `startswith` condition is true, it means that the reversed substring of `a` from index `i` to the end is a prefix of the original string `s`. This implies that the substring of `s` starting from the same index `i` and extending to the end is a palindrome.
* Therefore, the function returns the concatenation of the current substring of `a` (`a[:i]`) and the original string `s`. This represents the longest palindrome found so far.

**Step 5: No Palindrome Found**

* If no prefix match is found throughout the loop, the function reaches the end of the reversed string. This indicates that no palindrome was found within the original string.
* In such cases, the function simply returns the concatenation of the reversed string `a` and the original string `s`. This effectively combines the original string with its reversed version, which cannot be further extended to a longer palindrome.

**Overall Logic:**

* The algorithm iteratively checks for substrings common to both the original string and its reversed version.
* If a common prefix is found, it forms part of a palindrome within the original string.
* The process continues until the entire reversed string is scanned, ensuring the longest possible palindrome is identified.

**Time Complexity:** O(n^2)
* The nested loops involve comparisons of varying lengths, leading to quadratic complexity.

**Space Complexity:** O(n)
* The algorithm primarily utilizes the reversed string `a`, which takes up space proportional to the input string length.


</p>

## Hard 3
<p><strong>Question:</strong></p>
<p>Given an integer <code>n</code>, count the total number of digit <code>1</code> appearing in all non-negative integers less than or equal to <code>n</code>./p>
<p><strong>Solution:</strong></p>
<!-- tabs:start -->

#### **Python3**

```python
#Hard Program 3
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        a, x, res = n, 1, 0
        while a > 0:
            d = a % 10
            a //= 10  
            res += a * x
            if d == 1:
                res += n % x + 1
            elif d > 1:
                res += x
            x *= 10
        return res
n = 13
solution = Solution()
result = solution.countDigitOne(n)
print(result)

```
**Example Usage Output:**
```
n =  13
output = 6
```
<p><strong>Explanation of the code:</strong></p>
<p>
This code implements an algorithm to count the total number of occurrences of the digit "1" across all decimal representations of numbers from 1 to n (inclusive).

**Step 1: Base Case and Initialization**

* If `n <= 0`, it implies the range is empty, and no "1"s exist. The function returns 0 in this case.
* Otherwise, several variables are initialized:
    * `a`: Stores the original value of `n` for later comparisons.
    * `x`: Starts at 1 and represents the current power of 10.
    * `res`: Accumulates the total number of "1"s found throughout the loop.

**Step 2: Loop through Digits**

* A loop iterates while `a > 0`, meaning there are remaining digits to analyze.

**Step 3: Extract Current Digit**

* `d = a % 10` extracts the current digit (unit digit) from `a` using modulo operation.

**Step 4: Update variables**

* `a //= 10` removes the current digit from `a` by integer division, shifting focus to higher-order digits.
* `res += a * x` accounts for the "1"s in all numbers with higher-order digit greater than the current digit.

**Step 5: Special Cases for Current Digit**

* If `d == 1`:
    * This implies the current digit is "1", directly contributing to the count.
    * `res += n % x + 1` adds all "1"s in numbers from 1 to `n % x` with the same power of 10 as the current digit.
    * Additionally, 1 is added to account for the current number `n` itself.
* If `d > 1`:
    * This means the current digit is greater than "1".
    * `res += x` adds the number of "1"s contributed by all numbers within the current power of 10 (including those with a leading "1").

**Step 6: Update Power of 10**

* `x *= 10` increases the power of 10 for the next iteration, focusing on higher-order digits.

**Step 7: Return Result**

* After analyzing all digits, `res` contains the total number of "1"s.
* The function returns `res`.

**Overall Logic:**

* The algorithm iteratively analyzes each digit in `n` based on its value.
* It considers the contribution of "1"s in different cases, including those in higher-order digit positions and the current digit itself.
* By accumulating these contributions, the total number of "1"s across all numbers from 1 to n is determined.

**Time Complexity:** O(logn)
* The loop iterates through the number of digits in `n`, which is logarithmic to its value.

**Space Complexity:** O(1)
* The algorithm uses constant space for its variables, independent of the input size.



</p>


