class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

solve = Solution()
nums = [0,1,0,3,12]
solve.moveZeroes(nums)
print(nums)
# Output: [1,3,12,0,0]