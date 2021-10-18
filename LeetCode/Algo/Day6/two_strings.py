def commonCharacterCount(s1,s2):
    # SOLUTION 1: HASH-MAP 
        # dic1 = {}
        # for i in s1:
        #     if i in dic1:
        #         dic1[i] += 1
        #     else:
        #         dic1[i] = 1

        # dic2 = {}
        # for i in s2:
        #     if i in dic2:
        #         dic2[i] += 1
        #     else:
        #         dic2[i] = 1
            
        # count = 0
        
        # for i in dic1:
        #     if i in dic2:
        #         count += min(dic1[i], dic2[i])
        # return count
    # SOLUTION 2: 
    result = 0
    array1 = [0] * 52 # 26 if string is lowercase 
    array2 = [0] * 52 # 26 if string is lowercase
    for i in s1:
        array1[ord(i)-97] += 1
    for i in s2:
        array2[ord(i)-97] += 1
    for i in range(26):
        if array1[i] > 0 and array2[i] > 0:
            result += min(array1[i], array2[i])
    return result
    
print(commonCharacterCount('bABcc', 'adcAaa'))
