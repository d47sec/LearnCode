class Solution:
    def pivotIndex(self, nums) -> int:
        sumTotalArray = sum(nums)
        sumLeftArray = 0
        for i, arr in enumerate(nums):
            if sumLeftArray == sumTotalArray - arr - sumLeftArray:
                return i
            sumLeftArray += arr
        return -1
            

nums = [2,1,-1]
sol = Solution()
print(sol.pivotIndex(nums))
# Output: 0

