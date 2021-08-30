def count_change(money, coins):
    # your implementation here
    # Dynamic Programming
    ways = [1] + [0] * money
    for coin in coins:
        for i in range(coin, money + 1):
            ways[i] += ways[i - coin]
    return ways[money]

print(count_change(10, [2, 3, 5]))
# Link: https://www.codewars.com/kata/541af676b589989aed0009e7/train/python
