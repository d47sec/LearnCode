def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    temp = 0 
    for i in path:
        if i == 'U': temp += 1
        if i == 'D': temp -= 1
        if temp == 0 and i == 'U':
            valleys += 1
            
    return valleys

steps = 8
path = 'UDDDUDUU'
print(countingValleys(steps, path))
        


