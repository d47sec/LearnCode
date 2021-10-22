def sockMerchant(n, ar):
    dic = {}
    for val in ar:
        if val in dic:
            dic[val] += 1
        else:
            dic[val] = 1
    
    result = 0 
    for key in dic:
        result += (dic[key] // 2)
    return result

n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
print(sockMerchant(n, ar))