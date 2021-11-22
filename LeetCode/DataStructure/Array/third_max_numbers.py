class Solution:
    def thirdMax(self, nums) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
        
nums = [2,2,3,1]
solve = Solution()
print(solve.thirdMax(nums))