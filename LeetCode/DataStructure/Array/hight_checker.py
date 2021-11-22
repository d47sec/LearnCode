class Solution:
    def heightChecker(self, heights) -> int:

        arr = sorted(heights)
        k = 0 
        for i in range(len(heights)):
            if heights[i] != arr[i]:
                k  += 1
        return k 
    

nums =  [1,1,4,2,1,3]
solve = Solution()
print(solve.heightChecker(nums))        