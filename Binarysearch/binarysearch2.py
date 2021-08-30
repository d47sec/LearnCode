<<<<<<< HEAD
# def guess(num: int) -> int:

# class Solution:
#     def guessNumber(self, n: int) -> int:
#         l = 0
#         r = n
#         while(l <= n):
#             m = (l + r) // 2
#             if(guess(m) == 0):
#                 return m
#             elif(guess(m) == -1):
#                 r = m -1
#             else:
#                 l = m + 1

# # https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/
=======
# DAY 3
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while(l <= n):
            m = (l + r) // 2
            if(guess(m) == 0):
                return m
            elif(guess(m) == -1):
                r = m -1
            else:
                l = m + 1

# # https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/
>>>>>>> 5bf1aca1b0b9ded29bfd67fa46a4c108330edd7a
