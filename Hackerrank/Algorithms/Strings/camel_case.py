def camelcase(s):
    # Write your code here
    count = 1
    for character in s:
        if ord(character) <= 90 and ord(character) >= 65:
            count += 1
    return count


print(camelcase('thanhDatDo'))