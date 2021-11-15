def spiral(arr):
    top, left = 0 , 0 
    bottom, right = len(arr) - 1, len(arr[0]) - 1 
    res = []
    while top <= bottom and left <= right:
        
        for i in range(left, right+1):
            res.append(arr[top][i])
        top += 1

        for i in range(top, bottom+1):
            res.append(arr[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(arr[bottom][i])
            
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top -1, -1):
                res.append(arr[i][left])
            left += 1
            
    return res 


a = [[1, 2, 3, 18],
    [5, 6, 7, 17],
    [9, 10, 11,16]]

print(spiral(a))

# +) Ý TƯỜNG LÀ GÌ ? 
# - cần tạo bốn giá trị tương ứng với 4 góc: top, left, bottom, right
# - sau đó di chuyển từ trái sang phái : top += 1 
# - sau đó di chuyển từ trên xuống dưới: right -= 1
# - sau đó di chuyển từ phải sang trái : bottom -= 1
# - sau đó di chuyển từ dưới lên trên : left += 1 
