class Solution:
    def climbStairs(self, n: int) -> int:
        pre = 1 # n = 1
        curr = 2 # n = 2
        for i in range(3, n+1):
            sum = pre + curr
            pre = curr
            curr = sum 
        return curr
            
solve = Solution()
print(solve.climbStairs(3))

# bài này kiểu cho số n , tìm số cách để tống lại bằng n 
# các số chỉ có thể là 1, 2

# 2 => 1 + 1 , 2
# 3 => 1 + 1 + 1, 1 + 2, 2 + 1
# 1 1 2 3 5 8 13 