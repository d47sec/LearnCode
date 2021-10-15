class Solution:
    def maxArea(self, height) -> int:
        k = len(height)
        area = 0
        l = 0
        r = k - 1
        max_width = k - 1
        for width in range(max_width, 0, -1):
            if(height[l] < height[r]):
                area = max(area, width * height[l])
                l += 1
            else:
                area = max(area, width * height[r])
                r -= 1
        return area 
            
        
# Link: https://leetcode.com/problems/container-with-most-water/
# TWO POINTERS 
            
            
        