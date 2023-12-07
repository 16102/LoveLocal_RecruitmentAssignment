# Easy program 1
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
