class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            s = str(i)
            if '3' in s or '4' in s or '7' in s:
                continue
            if '2' in s or '5' in s or '6' in s or '9' in s:
                count += 1
        return count


# link: https://leetcode.com/problems/rotated-digits/
        
