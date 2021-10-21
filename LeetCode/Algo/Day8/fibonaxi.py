class Solution:
    # bad solution 
    def fib(self, n):
        if n == 0: 
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n - 2)
    
solve = Solution()
print(solve.fib(2))