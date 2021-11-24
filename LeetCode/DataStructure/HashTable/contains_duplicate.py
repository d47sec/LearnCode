class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
        return False

nums = [1,1,1,3,3,4,3,2,4,2]
solve = Solution()
print(solve.containsDuplicate(nums))