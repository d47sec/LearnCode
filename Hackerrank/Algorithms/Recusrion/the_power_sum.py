
#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    dp = [1] + [0] * X
    for i in range(1, int(pow(X, 1 / N)) + 1):
        u = i ** N
        for j in range(X, u - 1, -1):
            dp[j] += dp[j - u]
            print(dp)
    print(dp[-1])

# LOL vẫn chưa hiểu cái qq gì  để xem video lí thuyết đã

if __name__ == '__main__':
    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)
