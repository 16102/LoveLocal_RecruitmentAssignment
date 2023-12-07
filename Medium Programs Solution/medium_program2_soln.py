#Medium Program 2
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
