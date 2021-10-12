class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

nums = [1]
target = 0
solve = Solution()
print(solve.searchInsert(nums, target))

        