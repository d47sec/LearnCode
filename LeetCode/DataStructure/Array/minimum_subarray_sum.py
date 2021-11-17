class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        left = 0 
        sum = 0 
        ans = len(nums) + 1
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target and left <= right:
                ans = min(ans, right+1-left)
                sum -= nums[left]
                left += 1
        
        return ans if ans != len(nums)+1 else 0
       
        
solve = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(solve.minSubArrayLen(target, nums))