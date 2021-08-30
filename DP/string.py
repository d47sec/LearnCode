# def permute(s, answer):
#     if (len(s) == 0):
#         print(answer, end = "  ")
#         return
     
#     for i in range(len(s)):
#         ch = s[i]
#         left_substr = s[0:i]
#         right_substr = s[i + 1:]
#         rest = left_substr + right_substr
#         permute(rest, answer + ch)
 
# # Driver Code
# answer = ""
 
# s = input("Enter the string : ")
 
# print("All possible strings are : ")
# permute(s, answer)


# def per(a, res):
#     if len(a) == 0:
#         print(res)

#     for i in range(len(a)):
#         temp = a[i]
#         l = a[0:i]
#         r = a[i+1:]
#         remain = l + r 
#         per(remain, res+[temp])


# n = int(input('n: '))
# res = []
# per(list(range(1,n+1)), res)


def bina(k , n):
    for i in [0, 1]:
        res[k] = i 
        if  k == n - 1:
            print(res)
        else:
            bina(k + 1, n)

n = int(input('n: '))
res = [0] * n
bina(0, n)