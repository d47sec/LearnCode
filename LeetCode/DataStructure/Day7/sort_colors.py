class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        for i in range(red):
            nums[i] = 0 
        for i in range(white):
            nums[red+i] = 1
        for i in range(blue):
            nums[red+white+i] = 2
            
        return nums

    
solve = Solution()
print(solve.sortColors([2,0,2,1,1,0]))