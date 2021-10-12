class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) -1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right -= 1
            else:
                left += 1
        return -1