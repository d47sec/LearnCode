def repeatedString(s, n):
    
    length = len(s)
    repeated = n // length
    remainder = n % length
    count = 0
    for i in s:
        if i == 'a':
            count += 1
    count *= repeated
    for i in range(remainder):
        if s[i] == 'a':
            count += 1
    return count

print(repeatedString('a', 1000000000000))
        
        
    