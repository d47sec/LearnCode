from itertools import combinations

inputs = list(input().split(" "))

S = inputs[0]
k = int(inputs[1])

for i in range(1, k+1):
    for j in combinations(sorted(S), i):
        print(''.join(j))