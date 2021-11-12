class Solution:
    def plusOne(self, digits):
        result = str(int("".join([str(digit) for digit in digits])) + 1)
        return [int(i) for i in list(result)]
    
sol = Solution()
nums = [1,2,3,4]
print(sol.plusOne(nums))
        
        
        