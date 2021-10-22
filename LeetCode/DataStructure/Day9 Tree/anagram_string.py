def makeAnagram(a, b):
    dict_chars = {}
    for char in a:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1
    for char in b:
        if char in dict_chars:
            dict_chars[char] -= 1
        else:
            dict_chars[char] = -1
    
    sum_diff = 0
    
    for char in dict_chars.keys():
        sum_diff += abs(dict_chars[char])
        
    return sum_diff

print(makeAnagram('abcd', 'cde'))