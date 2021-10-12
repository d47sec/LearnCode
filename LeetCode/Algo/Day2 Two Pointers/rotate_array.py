class Solution:
    def rotate(self, nums, k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        while k:
            nums.insert(0, nums.pop())
            k -= 1

nums =[1, 2, 3, 4, 5, 6, 7]
k = 3
solve = Solution()
solve.rotate(nums, k)
print(nums)