class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # sử dụng kĩ thuật 2 pointers tiết kiệm được bộ nhớ hơn là cấp phát thêm mảng mới
        k = 0
        result = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                k += 1
            else:
                k = 0 
            result = max(result, k)
        return result
    

nums = [1,0,1,1,0,1]
solve = Solution()
print(solve.findMaxConsecutiveOnes(nums))