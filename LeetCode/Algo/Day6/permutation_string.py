
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sử dụng kĩ thuật mảng đánh dấu 
        if len(s1) > len(s2):
            return False
        array1 = [0] * 26
        for i in s1:
            array1[ord(i) - 97] += 1
        
        for i in range(len(s2)-len(s1)+1):
            array2 = [0] * 26 
            for j in range(len(s1)):
                array2[ord(s2[i+j])-97] += 1
            if self.match(array1, array2):
                return True
        return False
    
    def match(self, array1, array2):
        for i in range(26):
            if array1[i] != array2[i]:
                return False
        return True
        
           
solve = Solution()
print(solve.checkInclusion('ab', 'eidbaooo'))

# https://leetcode.com/problems/permutation-in-string/