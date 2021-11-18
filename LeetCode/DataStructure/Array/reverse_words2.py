class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split(" ")
        result = ''
        for i in temp:
            result += i[::-1] + " "
        # print(result)
        return result[:-1]
    
    
solve = Solution()
print(solve.reverseWords("Let's take LeetCode contest"))