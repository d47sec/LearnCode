class Solution:
    def maxProfit(self, prices) -> int:
        # SOLUTION 1: Brute force
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit 
        # return max_profit
    
        # SOLUTION 2:
        max_profit = 0 
        buy = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - buy 
            if profit > max_profit:
                max_profit = profit 
            if prices[i] < buy :
                buy = prices[i]
        return max_profit
        
                
solve = Solution()
prices = [7,6,4,3,13]
print(solve.maxProfit(prices))