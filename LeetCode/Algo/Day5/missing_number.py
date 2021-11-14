class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        # sum of nums from 1 to n 
        
        sum_n = n * (n+1) // 2
        for num in nums:
            sum_n -= num
        return sum_n
                
solve = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(solve.missingNumber(nums))
# https://leetcode.com/problems/missing-number/