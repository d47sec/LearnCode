class Solution:
    def removeElement(self, nums, val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        # for i in range(k):
        #     print(nums[i])
        return k 


solve = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(solve.removeElement(nums, val))