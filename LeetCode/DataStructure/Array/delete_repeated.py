class Solution:
    def deleteReapted(self, nums):
        
        writePointer = 1
        for readPointer in range(1, len(nums)):
            if nums[readPointer] != nums[readPointer-1]:
                nums[writePointer] = nums[readPointer]
                writePointer += 1

        return nums[:writePointer]
    
nums = [0,0,1,1,2,3,3]
solve = Solution()
print(solve.deleteReapted(nums))
    
    