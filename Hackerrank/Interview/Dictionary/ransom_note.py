def checkMagazine(magazine, note):
    # Write your code here
    dic = {}
    for i in note:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in magazine:
        if i in dic:
            dic[i] -= 1
    for i in dic:
        if dic[i] > 0:
            print("No")
            return
    print("Yes")
    