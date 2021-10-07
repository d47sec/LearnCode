from itertools import permutations
# permutations là hàm dùng để hoán vị các phần tử trong một iterator 
value = list(input().split(" "))
S = value[0]
k = int(value[1])
# print(list(permutations(S, k)))

array = []
for i in list(permutations(S,k)):
    array.append(''.join(i))
array.sort()
for i in array:
    print(i)