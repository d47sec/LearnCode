class Solution:
    def sortedSquares(self, nums):
        return sorted([i*i for i in nums])

# bài nào đơn giản được thì đơn giản two pointer bài này rắc rồi :)))

solve = Solution()
nums = [-1, -2, 0, 1, 2, 4]
print(solve.sortedSquares(nums))

