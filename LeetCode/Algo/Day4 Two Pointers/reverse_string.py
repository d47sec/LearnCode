class Solution:
    def reverseString(self, s):
        left,  right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
            

solve = Solution()
s = ["a", "b", "c", "d"]
solve.reverseString(s)
print(s)
# s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]