class Solution:
    def reverseString(self, s) -> None:
        l, r = 0 , len(s)-1
        
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s
    
    
solve = Solution()
s = ['a', 'b', 'c', 'd', 'e']
print(solve.reverseString(s))