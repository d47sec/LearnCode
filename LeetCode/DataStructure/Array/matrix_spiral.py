def spiral(arr):
    top, left = 0 , 0 
    bottom, right = len(arr) - 1, len(arr) - 1 
    res = []
    while top <= bottom and left <= right:
        for i in range(left, right+1):
            res.append(arr[top][i])
        top += 1

        for i in range(top, bottom+1):
            res.append(arr[i][right])
        right -= 1

        for i in range(right, left - 1, -1):
            res.append(arr[bottom][i])
        
        bottom -= 1

        for i in range(bottom, top -1, -1):
            res.append(arr[i][left])
        
        left += 1

    return res 


a = [[1, 2, 3, 18],
    [5, 6, 7, 17],
    [9, 10, 11,16],
    [12,13,14,15]]

print(spiral(a))