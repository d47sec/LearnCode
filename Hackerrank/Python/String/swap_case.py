def swap_case(s):
    res = ''
    for c in s:
        if c.isupper():
            res += c.lower()
        else:
            res += c.upper()
    return res 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true