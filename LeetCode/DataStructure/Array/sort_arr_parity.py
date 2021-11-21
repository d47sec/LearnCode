class Solution:
    def sortArrayByParity(self, nums):
        k = 0 
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[k],nums[i] = nums[i], nums[k]
                k += 1
        return nums
        
    


solve = Solution()
nums = [0]
print(solve.sortArrayByParity(nums))
        