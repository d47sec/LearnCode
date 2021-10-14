class Solution:
    def maxSubArray(self, nums) -> int:
        max_so_far = nums[0]
        curr_max = nums[0]
        for i in range(1,len(nums)):
           curr_max = max(nums[i], curr_max + nums[i])
           if curr_max > max_so_far:
               max_so_far = curr_max
        return max_so_far
               
nums = [-2,1,-3,4,-1,2,1,-5,4]
solve = Solution()
print(solve.maxSubArray(nums))


# CODE JAVA:
# class Solution {
#     public int maxSubArray(int[] nums) {
#         int max_current = nums[0];
#         int max_so_far = nums[0];
#         for(int i = 1; i < nums.length; i++){
#             max_current = Math.max(nums[i], nums[i] + max_current);
#             if(max_current > max_so_far){
#                 max_so_far  = max_current;
#             }
#         }
#         return max_so_far;
#     }
# }