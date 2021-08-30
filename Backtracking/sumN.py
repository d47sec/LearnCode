def solv():
    n = 6
    res = [0] * n 
    def backtrack(k, n):
        for i in range(1, n+1):
            res[k] = i
            if sum(res) == n:
                print(res)
                n - 1
            else:
                backtrack(k+1, n)
    return backtrack(0, n)

solv()