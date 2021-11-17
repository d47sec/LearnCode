from typing import Mapping, MappingView, Match


class Solution:
    def rotate(self, nums, k: int) -> None:
        
        # SOLUTION 1 với mảng lớn sẽ bị TLE 
        # def rotateOne(nums):
        #     tmp = nums[len(nums)-1]
        #     for i in range(len(nums)-1,-1,-1):
        #         nums[i] = nums[i-1]
        #     nums[0] = tmp
        #     # return nums
        
        # for i in range(k):
        #     rotateOne(nums)
        
        # return nums
    
        # SOLUTION 2
        def solve(nums, i, j):
            while i < j :
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1        
        solve(nums, 0, len(nums)-1)
        print(nums)
        solve(nums, 0, k-1)
        print(nums)
        solve(nums, k, len(nums)-1)
        return nums
        
    
solve = Solution()
nums = [1,2,3,4,5]
k  = 3
print(solve.rotate(nums, k))
                
            