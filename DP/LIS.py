def solv(arr, n):
    res = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if(arr[i] > arr[j] and res[i] < res[j] + 1):
                res[i] += 1
    
    return max(res)

arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print("Length of lis is ", solv(arr, n))

