class Solution:
    def containsDuplicate(self, nums) -> bool:
        sets = set(nums)
        return True if len(nums) != len(sets) else False

nums = [1,1,1,3,3,4,3,2,4,2]
solve = Solution()
print(solve.containsDuplicate(nums))