# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = list(int(i) for i in input().split(" "))
B = list(int(i) for i in (input().split(" ")))
# (print(i) for i in list(product(A,B)))
# hàm product này giống như tính tích đề cát của 2 vector 
# VÍ DỤ:
# A = [1, 2]
# B = [3, 4]
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]

C = list(product(A,B))
for i in C:
    print(i, end=" ")