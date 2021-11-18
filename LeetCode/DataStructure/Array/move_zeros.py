class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        for j in range(1,len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        return nums

solve = Solution()
nums = [3,1,0,3,12]
print(solve.moveZeroes(nums))