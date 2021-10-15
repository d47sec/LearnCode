class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(0,len(s),2*k):
            arr[i:i+k] = reversed(arr[i:i+k])
            print(arr[i:i+k])
        return ''.join(arr)
        
s = "abcdefg"
k = 2
solve = Solution()
print(solve.reverseStr(s,k))
# Output: "bacdfeg"

