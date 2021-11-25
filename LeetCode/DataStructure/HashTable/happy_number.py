class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            sum_of_N = 0
            while n > 0:
                n,mod= divmod(n, 10)
                sum_of_N += mod ** 2
            return sum_of_N
        
        
        hashSet = set()
        while n != 1 and n not in hashSet:
            hashSet.add(n)
            n = getNext(n)
        
        return n == 1
            
solve = Solution()
print(solve.isHappy(100))

# https://leetcode.com/problems/happy-number/solution/