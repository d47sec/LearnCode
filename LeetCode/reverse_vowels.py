class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'U', 'I', 'O']
        # l , r = 0, len(s) - 1
        s  = list(s)
        def helper(l, r):
            if l < r:
                if s[l] not in vowels:
                    l += 1
                elif s[r] not in vowels:
                    r -= 1
                else:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                helper(l, r)
        helper(0, len(s) - 1)
        return ''.join(s)
            

# link: https://leetcode.com/problems/reverse-vowels-of-a-string/
        