class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        result = [0] * len(nums)
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            result[i] = max(nums[i] + result[i-2], result[i-1])
            print(result)
        return result[len(nums)-1]

nums = [1,2,3,1]
solve = Solution()
print(solve.rob(nums))
