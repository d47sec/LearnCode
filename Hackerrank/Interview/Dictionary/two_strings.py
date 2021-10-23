def twoStrings(s1, s2):
    # Write your code here
    dic = {}
    for i in s1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in s2:
        if i in dic:
            return 'YES'
    return 'NO'