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