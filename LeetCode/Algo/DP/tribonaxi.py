class Solution:
    def tribonacci(self, n: int) -> int:
        result = [0] * (n+1)
        result[0] = 0
        result[1] = 1
        result[2] = 1
        for i in range(3, n+1):
            result[i] = result[i-1] + result[i-2] + result[i-3] 
        return result[n]
    
solve = Solution()
print(solve.tribonacci(2))