class Solution:
    def dominantIndex(self, nums) -> int:
        maxIndex = 0
        maxValue = 0
        for i, num in enumerate(nums):
            if num > maxValue:
                maxValue = num
                maxIndex = i 
        for num in nums:
            if num != maxValue and num * 2 > maxValue:
                return -1
        return maxIndex
        

nums=[1,2,3,4]
sol = Solution()
print(sol.dominantIndex(nums))

# https://leetcode.com/explore/learn/card/array-and-string/