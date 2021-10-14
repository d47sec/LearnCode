class Solution:
    def maxSubArray(self, a) -> int:
        
        max_so_far = a[0]
        curr_max = a[0]
        
        for i in range(1,len(a)):
            print("current max: " + str(curr_max))
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)
        return max_so_far

nums = [5,4,-1,7,8]
solve = Solution()
print(solve.maxSubArray(nums))
