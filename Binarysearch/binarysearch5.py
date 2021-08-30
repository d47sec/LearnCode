<<<<<<< HEAD
# DAY 5
class Solution:
    def findPeakElement(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while(l < r):
            mid = (l + r) // 2
            if(nums[mid] > nums[mid + 1]):
                r = mid
            else:
                l = mid + 1
        return r

s = Solution()
print(s.findPeakElement([1, 2, 3, 4]))

# https://leetcode.com/problems/find-peak-element/


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while(l < r):
            mid = (r + l) // 2
            if(arr[mid] > arr[mid + 1]):
                r = mid
            else:
                l = mid + 1
        return l

# https://leetcode.com/problems/peak-index-in-a-mountain-array/

=======
# DAY 5
class Solution:
    def findPeakElement(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while(l < r):
            mid = (l + r) // 2
            if(nums[mid] > nums[mid + 1]):
                r = mid
            else:
                l = mid + 1
        return r
        
s = Solution()
print(s.findPeakElement([1, 2, 3, 4]))

# https://leetcode.com/problems/find-peak-element/
>>>>>>> 5bf1aca1b0b9ded29bfd67fa46a4c108330edd7a
