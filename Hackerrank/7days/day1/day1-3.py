def timeConversion(s):
    # Write your code here
    result = ''
    if s[-2:] == "AM" :
            if s[:2] == '12':
                result= str('00' + s[2:8])
            else:
                result= s[:-2]
    else:
        if s[:2] == '12':
            result= s[:-2]
        else:
            result= str(int(s[:2]) + 12) + s[2:8]
    return result

print(timeConversion("12:05:45AM"))