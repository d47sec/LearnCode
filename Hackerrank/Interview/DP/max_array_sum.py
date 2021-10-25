def maxSubsetSum(arr):
    
    result = [0] * len(arr)
    result[0] = arr[0]
    result[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        result[i] = max(result[i-2] + arr[i], result[i-1], arr[i])
    return result[len(arr)-1]

nums = [-2, -3, -1]
print(maxSubsetSum(nums))