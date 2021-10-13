class Solution:
    def sortedSquares(self, nums):
        left, right, i = 0, len(nums) - 1, len(nums) - 1
        output = [0] * len(nums)
        while left <= right:
            a = nums[left] * nums[left]
            b = nums[right] * nums[right]
            if a > b:
                output[i] = a
                left += 1
            else:
                output[i] = b
                right -= 1
            i -= 1
        return output

# Độ phức tạp thuật toán là 0(log(n))
# Độ phức tạp bộ nhớ là 0(N)
solve = Solution()
nums = [-4,-1,0,3,5]
print(solve.sortedSquares(nums))

