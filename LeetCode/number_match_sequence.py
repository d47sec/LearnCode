# BRUTE FORCE (TLE) 
# class Solution:
#     def numMatchingSubseq(self, s: str, words) -> int:
#         count = 0 
#         def sequence(s, word):
#             x, y = 0, 0
#             while x < len(s) and y < len(word):
#                 if s[x] == word[y] :  
#                     x += 1 
#                     y += 1
#                 else:
#                     x += 1
#             return y == len(word)
            
#         for word in words:
#             if(sequence(s, word)):
#                 count += 1

#         return count 
import collections
class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        waiting = collections.defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])
                
sol = Solution()
print(sol.numMatchingSubseq("abcde",  ["a","bb","acd","ace"] ))

# link: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3788/