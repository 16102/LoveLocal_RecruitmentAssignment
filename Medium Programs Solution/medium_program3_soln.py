#Medium Program 3
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