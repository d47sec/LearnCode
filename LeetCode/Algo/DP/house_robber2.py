class Solution:
    def rob(self, nums) -> int:
        def solve(self, nums)->int:
            result = [0] * len(nums)
            result[0] = nums[0]
            result[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                result[i] = max(result[i-1], result[i-2] + nums[i])
            return result[len(nums)-1]
        
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        max1 = solve(self,nums[1:])
        max2 = solve(self, nums[:-1])
        return max(max1, max2)
    
solve = Solution()
nums = [1,2,3,1]
print(solve.rob(nums))