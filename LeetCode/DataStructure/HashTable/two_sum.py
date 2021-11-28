class Solution:
    def twoSum(self, nums, target: int):
        dict = {}
        for i, num in enumerate(nums):
            val = target - nums[i]
            if val not in dict:
                dict[num] = i 
            else:
                return [dict[val], i]
                
solve = Solution()
nums = [2,7,11,15]
target = 9

print(solve.twoSum(nums, target))
        