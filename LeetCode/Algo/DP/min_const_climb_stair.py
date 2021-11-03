class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        n = len(cost)
        dp = [0] * (n)
        dp[0] = cost[0]
        dp[1] = cost[1]
        print(dp)
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        # print(dp)
        return min(dp[-1], dp[-2])

solve = Solution()
nums = [10, 15, 30]
print(solve.minCostClimbingStairs(nums))