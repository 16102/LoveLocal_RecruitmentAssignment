#Hard Program 2
class Solution:
    def findPalindrome(self, s: str) -> str:
        a = s[::-1]

        for i in range(len(a)):
            if s.startswith(a[i:]):
                return a[:i] + s

        return a + s

#Example Usage
s = "aacecaaa"
solution = Solution()
result = solution.findPalindrome(s)
print(result)