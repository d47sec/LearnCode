# Đề bài: cho một mảng đã được rotated ==> có nghĩa là ban đầu đã được sắp xếp sau đó rotated 
# Cho giá trị x , nếu x ở trong mảng rotated thì return ra vị trí ở trong mảng đó, còn ko thì return - 1
# nhiệm vụ bây giờ là cần tìm ra vị trí có giá trị nhỏ nhất 

def solve(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1 

def find_pivot(array):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < array[-1]:
            right = mid - 1
        else:
            left = mid + 1
    return left

array = [9, 10 ,13, 0, 1, 2, 3, 7]
target = 0
pivot = find_pivot(array)
f1 = solve(array[:pivot], target)
f2 = solve(array[pivot:], target)

if f1 == -1 and f2 == -1:
    print(-1)
elif f1 != -1:
    print(f1)
else:
    print(f2 + pivot)
