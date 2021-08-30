# DAY 7
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = dict()
        val = ""
        for i in range(len(s)):
            if(s[i] not in dic):
                if(t[i] not in val):
                    dic[s[i]] = t[i]
                    val += t[i]
                else:
                    return False
            else:
                if(t[i] != dic[s[i]]):
                    return False
        return True

solve = Solution()
print(solve.isIsomorphic("egg","ads"))

# https://leetcode.com/problems/isomorphic-strings/

# DAY 7
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = dict()
        val = ""
        for i in range(len(s)):
            if(s[i] not in dic):
                if(t[i] not in val):
                    dic[s[i]] = t[i]
                    val += t[i]
                else:
                    return False
            else:
                if(t[i] != dic[s[i]]):
                    return False
        return True

solve = Solution()
print(solve.isIsomorphic("egg","ads"))

# https://leetcode.com/problems/isomorphic-strings/
