# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = list(int(i) for i in input().split(" "))
B = list(int(i) for i in (input().split(" ")))
# (print(i) for i in list(product(A,B)))
C = list(product(A,B))
for i in C:
    print(i, end=" ")