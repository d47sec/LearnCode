class Solution:
    # SOLUTION 1:
    def rotate(self, nums, k: int):
        # đang sử dụng high function vì sài function trong function 
        def twopt(arr, i, j):
            # function này có chức năng chia mảng thành 2 bên sau đó hoán đổi giá trị của 2 mảng con này cho nhau 
            while i < j:
                arr[i] , arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return arr
        
        if k > 0:
            twopt(nums, 0, len(nums)-1) # xoay toàn bộ mảng
            # print(nums)
            twopt(nums, 0, k -1) # xoay số phần tử cần phải xoay theo yêu cầu đề
            # print(nums)
            twopt(nums, k, len(nums)-1) # xoay số phần tử còn lại trong mảng
            
    # SOLUTION 2:
    def rotateLeftByOne(self, nums):
        temp = nums[0]
        for i in range(len(nums)-1):
            nums[i] = nums[i+1]
        nums[len(nums)-1] = temp
    def leftRotate(self, nums, k):
        for i in range(k):
            self.rotateLeftByOne(nums)
            
    def rotateRightByOne(self, nums):
        temp = nums[len(nums)-1]
        for i in range(len(nums)-1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = temp
        
    def rightRotate(self, nums, k):
        for i in range(k):
            self.rotateRightByOne(nums)
            
            
nums = [-4, -3, -2, 0, 1, 2]
k = 2
solve = Solution()
# solve.leftRotate(nums, k)
# print(nums)
solve.rightRotate(nums,k)
print(nums)