
class Solution:
    def sum(self, nums, target):
        hashtable = {}
        res = []
        for i, num in enumerate(nums):
            remain = target - num
            if(remain not in hashtable):
                hashtable[num] = i
            else:
                res.append([hashtable[remain], i])
        return res

solve = Solution()
print(solve.sum([1,2,3,4], 5))

class Solution:
    def sum(self, nums, target):
        hashtable = {}
        res = []
        for i, num in enumerate(nums):
            remain = target - num
            if(remain not in hashtable):
                hashtable[num] = i
            else:
                res.append([hashtable[remain], i])
        return res

solve = Solution()
print(solve.sum([1,2,3,4], 5))
