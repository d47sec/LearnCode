def stepPerms(n):
    # Write your code here
    result = [0] * max(n+1, 4)
    result[1] = 1
    result[2] = 2
    result[3] = 4
        
    for i in range(4,n+1):
        result[i] = result[i-1] + result[i-2] + result[i-3]
    return result[n]
