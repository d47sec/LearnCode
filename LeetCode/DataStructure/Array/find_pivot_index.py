class Solution:
    def pivotIndex(self, nums) -> int:
        sumR = sum(nums)
        sumL = 0 
        for i, arr in enumerate(nums):
            if sumL == sumR - arr - sumL:
                return i 
            sumL += arr
        return -1
            

nums = [2,1,-1]
sol = Solution()
print(sol.pivotIndex(nums))
# Output: 0

