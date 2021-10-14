class Solution:
    # Solution 1
    def twoSum(self, numbers, target: int):
        left , right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

    # Solution 2:
    def twoSum2(self, numbers, target):
        dic = {}
        for i, j in enumerate(numbers):
            if j in dic:
                return [dic[j]+1, i+1]
            dic[target-j] = i 
        
solve = Solution()
numbers = [2,7,11,15]
target = 9
print(solve.twoSum2(numbers, target))
# link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/