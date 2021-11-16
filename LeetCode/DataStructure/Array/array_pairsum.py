class Solution:
    def arrayPairSum(self, nums) -> int:
        nums = sorted(nums)
        # print(nums)
        # print(nums[::2])
        # return sum(nums[::2])
        result = 0
        l, r = 0, 1
        while l < len(nums)-1:
            result += min(nums[l], nums[r])
            l += 2
            r += 2
        return result
    

solve = Solution()
nums = [6,2,6,5,1,2]
print(solve.arrayPairSum(nums))