class Solution:
    def singleNumber(self, nums) -> int:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                hashSet.remove(num)
            else: hashSet.add(num)
        return list(hashSet)[0]
        

nums = [1,2,2]
solve = Solution()
print(solve.singleNumber(nums))