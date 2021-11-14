import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # SOLUTION 1:
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1 
        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1
        # SOLUTION 2
        # count = collections.Counter(s)
        # print(count)
        # # find the index
        # for idx, ch in enumerate(s):
        #     if count[ch] == 1:
        #         return idx     
        # return -1
        
solve = Solution()
print(solve.firstUniqChar('loveleetcode'))
                