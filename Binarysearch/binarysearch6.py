# <<<<<<< HEAD
# DAY 6 
class Solution:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while(l < r):
            mid = (l + r) // 2
            if(nums[mid] < nums[r]):
                r = mid
            else:
                l = mid + 1
        return nums[l]
        
solve = Solution()

print(solve.findMin([4, 5, 6, 7, 0, 1, 2]))

# =======
# DAY 6 
class Solution:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while(l < r):
            mid = (l + r) // 2
            if(nums[mid] < nums[r]):
                r = mid
            else:
                l = mid + 1
        return nums[l]
        
solve = Solution()

print(solve.findMin([4, 5, 6, 7, 0, 1, 2]))

# >>>>>>> 5bf1aca1b0b9ded29bfd67fa46a4c108330edd7a
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/