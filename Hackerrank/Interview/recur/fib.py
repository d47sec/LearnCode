def fibonacci(n):
    
    # Write your code here.
    result = [0] * (n+1)
    result[0] = 1
    result[1] = 1
    for i in range(2, n+1):
        result[i] = result[i-1] + result[i-2]
    print(result)
    return result[n-1]

n = int(input())
print(fibonacci(n))