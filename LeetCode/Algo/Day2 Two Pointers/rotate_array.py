class Solution:
    def rotate(self, nums, k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        def twopt(arr, i, j):
            while i < j:
                arr[i] , arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return arr
        if k > 0:
            twopt(nums, 0, len(nums)-1)
            print(nums)
            twopt(nums, 0, k -1)
            print(nums)
            twopt(nums, k, len(nums)-1)
            
                
nums =[-4, -3, -2, 0, 1, 2]
k = 3
solve = Solution()
solve.rotate(nums, k)
print(nums)