def rotLeft(a, d):
    # Solution 1
    return a[d:] + a[:d]
    # Solution 2
    for i in range(d):
        rot(a)
    return a

def rot(a):
    temp = a[0]
    for i in range(1, len(a)):
        a[i-1] = a[i]
    a[len(a)-1] = temp
    return a
    
nums = [1,2,3,4,5]
d = 4
print(rotLeft(nums, d))

# 5 4
# 1 2 3 4 5