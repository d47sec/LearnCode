class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in s:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        for i in t:
            if i in dic2:
                dic2[i] += 1
            else:
                dic2[i] = 1
        # print(dic1)
        # print(dic2)
        if len(dic1) != len(dic2):
            return False
        for i in dic1:
            if i in dic2 and dic1[i] == dic2[i]:
                continue
            else:
                return False
        return True    

solve = Solution()
print(solve.isAnagram("rat", "car"))