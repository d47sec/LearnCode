class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        res = [0] * (n+1)
        res[0] = 0
        res[1] = 1
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]
    
solve = Solution()
print(solve.fib(50))

# 0 1 1 2 3 5 