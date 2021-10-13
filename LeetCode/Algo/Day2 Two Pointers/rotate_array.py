class Solution:
    def rotate(self, nums, k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        # đang sử dụng high function vì sài hàm trong hàm 
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
            
nums =[-4, -3, -2, 0, 1, 2]
k = 2
solve = Solution()
solve.rotate(nums, k)
print(nums)