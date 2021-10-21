class Solution:
    def climbStairs(self, n: int) -> int:
        
        # dynamic programming 
        res = [0] * n 
        res[0] = 1
        res[1] = 1
        for i in range(2, n):
            j = 1
            while j <= 2 and j <= i:
                res[i] = res[i] + res[i-j]
                j += 1
        print(res)
        return res[n-1]

solve = Solution()
print(solve.climbStairs(3))

# bài này kiểu cho số n , tìm số cách để tống lại bằng n 
# các số chỉ có thể là 1, 2

# 2 => 1 + 1 , 2
# 3 => 1 + 1 + 1, 1 + 2, 2 + 1
# 1 1 2 3 5 8 13 