# Easy Program 3

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
