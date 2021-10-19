# link: https://luyencode.net/problem/USEQ?fbclid=IwAR0MmIKg9iqp5Y-tZ4SezVrGbnQg9lPBrb5lMbrwGwDQK5LNp0jEI4uuSdk

def solved(N, Array):
    dic = {}
    for i in Array:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in dic:
        if dic[i] % 2 != 0:
            return i 

N = int(input())
Array = list(input().split(" "))
print(solved(N, Array))
    
# Đề bài: tìm giá trị có tần suất xuất hiện lẻ ở trong mảng 