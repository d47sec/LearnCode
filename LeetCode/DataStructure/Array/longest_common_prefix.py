class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        strs.sort()
        # print(strs)
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            print(x, y)
            if x == y: p+=x
            else: break
        return p
    

solve = Solution()
strs =  ["flower","flow","flight"]
print(solve.longestCommonPrefix(strs))

# Python ba vl 