class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split(" ")
        result = ""
        for i in temp:
            result += i[::-1] + " "
        return result[:-1]

s = "Let's take LeetCode contest"
solve = Solution()
print(solve.reverseWords(s))
# Output: "s'teL ekat edoCteeL tsetnoc"