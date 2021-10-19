# link: https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/



class Solution:
    def duplicateZeros(self, arr):
        i = 0
        while i < len(arr)-1:
            if arr[i] == 0:
                for j in range(len(arr)-1,i,-1):
                    arr[j] = arr[j-1]
                i += 1
            i += 1
        return arr
                    
arr = [1,0,2,3,0,4,5,0]
arr = [1,2,3]
solve = Solution()
print(solve.duplicateZeros(arr))

# Output: [1,0,0,2,3,0,0,4]