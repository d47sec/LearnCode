N = int(input().strip())
H = list(int(i) for i in input().split(" "))

res = [0] * (N+1)
res[1] = abs(H[1] - H[0])
for i in range(2,N):
    res[i] = min(res[i-1]+abs(H[i] - H[i-1]), res[i-2] +abs(H[i]-H[i-2]))
print(res[N-1])


# link: https://luyencode.net/problem/STONEFROG1