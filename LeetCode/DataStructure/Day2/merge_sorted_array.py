class Solution:
    def merge(self, nums1 , m, nums2 , n):
        l = m + n - 1
        while m > 0 and n > 0:
            print(m, n)
            if nums2[n-1] > nums1[m-1]:
                nums1[l] = nums2[n-1]
                l -= 1
                n -= 1
            else:
                nums1[l] = nums1[m-1]
                l -= 1
                m -= 1
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1
        return nums1

solve = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [1,3,5]
n = 3
print(solve.merge(nums1, m, nums2, n))