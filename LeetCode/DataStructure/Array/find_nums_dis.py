class Solution:
    def findDisappearedNumbers(self, nums):
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        result = []
        for i in range(1, len(nums)+1):
            if i not in dict:
                result.append(i)
    
        return result
    

nums = [4,3,2,7,8,2,3,1]
solve = Solution()
print(solve.findDisappearedNumbers(nums))
            
            
        