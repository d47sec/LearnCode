class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i,num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            dic[target-num] = i     
        return dic
    
nums = [3, 2, 1, 4, 5]
target = 6
solve = Solution()
print(solve.twoSum(nums, target))
