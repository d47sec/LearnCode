class Solution:
    def searchRange(self, nums, target: int):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                while mid >= 0 and nums[mid] == target:
                    mid -= 1
                mid += 1
                start = mid
                while mid <= r and nums[mid] == target:
                    mid +=1
                mid -= 1
                end = mid
                return [start, end]
            else:
                l = mid + 1
        return [-1, -1]
        
solve = Solution()
print(solve.searchRange([1,2], 1))

# Link: https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/