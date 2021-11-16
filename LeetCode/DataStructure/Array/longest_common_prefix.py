class Solution:
    def longestCommonPrefix(self, strs) -> str:
        
        # =============== SOLUTION 1 ======================
        # +) Ý tưởng đoạn code này là tìm LCP(LCP(s1,s2),s3) ....
        # prefix = strs[0]
        
        # for i in range(1, len(strs)):
        #     while (strs[i]).find(prefix) != 0:
        #         prefix = prefix[0 : len(prefix)-1]
        #         if prefix == "": return ""
        # return prefix
    
        # ================= SOLUTION 2 =======================
        # +) Sài divide and conquer để xử lí bài toán này : LCP(S1, ..., Sn) = LCP(LCP(S1, Sk) ,LCP(Sk, Sn))
        
        
        
        # Sài binary search để solve bài nào cũng oke
        # ================== SOLUTION 3 ======================
        def binarySearchLCP(strs):
            minLen = len(min(strs))
            l = 1
            r = minLen
            while l <= r:
                mid = (l + r) // 2
                if commonPrefix(strs, mid):
                    l = mid + 1
                else:
                    r = mid - 1
            return strs[0][0:(l+r)//2]
        
        
        def commonPrefix(s, lenght):
            prefix = s[0][0:lenght]
            for i in range(1, len(s)):
                if not s[i].startswith(prefix):
                    return False
            return True
                    
        return binarySearchLCP(strs)
        


solve = Solution()
strs =  ["c","acc","ccc"]
print(solve.longestCommonPrefix(strs))

