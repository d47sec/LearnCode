def findMedian(arr):
    arr = sorted(arr)
    print(arr)
    return arr[len(arr) // 2] 

print(findMedian([34,2,3,4,5]))
# passed