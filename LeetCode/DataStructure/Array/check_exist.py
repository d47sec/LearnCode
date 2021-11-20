class Solution:
    def checkIfExist(self, arr) -> bool:
        
        for i in range(len(arr)):
            if arr[i] % 2 == 0 :
                for j in range(len(arr)): 
                    if j != i and arr[j] * 2 == arr[i]:
                        return True
        return False
        
        
        
        
solve = Solution()
arr = [10,2,5,3]

print(solve.checkIfExist(arr))