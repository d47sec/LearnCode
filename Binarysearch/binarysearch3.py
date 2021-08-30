# <<<<<<< HEAD
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l <= r):
            mid = int((r+l)/2)
            if(nums[mid] == target): # case 1: tìm được target
                return mid
            if(nums[mid] <= nums[r]):  # case 2: một nữa bên phải đã được sắp sếp
                if(target >= nums[mid] and target <= nums[r]):
                    l = mid + 1 # đi tìm nữa bên phải
                else:
                    r = mid - 1 # đi tìm nữa bên trái
            if(nums[mid] >= nums[l]): # case 3: một nữa bên trái đã được sắp sếp
                if(target >= nums[l] and target <= nums[mid]):
                    r = mid - 1 # đi tìm nữa bên trái
                else:
                    l = mid + 1 # đi tìm nữa bên phải
        return -1
                

# bài này trên leetcode Search in Rotated Sorted Array
# https://leetcode.com/explore/learn/card/binary-search/125/template-i/952
# =======
# DAY 3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l <= r):
            mid = int((r+l)/2)
            if(nums[mid] == target): # case 1: tìm được target
                return mid
            if(nums[mid] <= nums[r]):  # case 2: một nữa bên phải đã được sắp sếp
                if(target >= nums[mid] and target <= nums[r]):
                    l = mid + 1 # đi tìm nữa bên phải
                else:
                    r = mid - 1 # đi tìm nữa bên trái
            if(nums[mid] >= nums[l]): # case 3: một nữa bên trái đã được sắp sếp
                if(target >= nums[l] and target <= nums[mid]):
                    r = mid - 1 # đi tìm nữa bên trái
                else:
                    l = mid + 1 # đi tìm nữa bên phải
        return -1
                

# bài này trên leetcode Search in Rotated Sorted Array
# https://leetcode.com/explore/learn/card/binary-search/125/template-i/952
# >>>>>>> 5bf1aca1b0b9ded29bfd67fa46a4c108330edd7a
