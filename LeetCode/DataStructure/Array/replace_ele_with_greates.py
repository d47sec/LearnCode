class Solution:
    def replaceElements(self, arr):
        tillMax = arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            tillMax, arr[i] = max(tillMax, arr[i]), tillMax
        
        arr[len(arr)-1] = -1
        return arr
    
nums = [17,18,5,4,6,1]
solve = Solution()
print(solve.replaceElements(nums))

# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/

        
        