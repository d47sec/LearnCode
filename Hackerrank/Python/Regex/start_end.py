import re 
S = input()
k = input()

reg = r'\w+'
res = (re.findall(k, S))

print(res)

