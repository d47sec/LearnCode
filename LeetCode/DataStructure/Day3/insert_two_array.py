import time
class Solution:
    # SOLUTION 1:
    def intersect(self, nums1, nums2):
        nums1.sort() # ĐPT: O(Nlog(N))
        nums2.sort() # ĐPT: O(Nlog(N))
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
                continue
            if nums1[i] > nums2[j]:
                j += 1
                continue
            res.append(nums1[i])
            i += 1
            j += 1
        return res
    # SOLUTION 2: Cách này nhanh hơn 
    def intersect2(self, nums1, nums2):
        dic = {}
        res = []
        for num in nums1:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for num in nums2:
            if num in dic and dic[num] > 0:
                res.append(num)
                dic[num] -= 1
        return res
                
# ĐỘ PHỨC TẠP O(nlog(n))
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
solve = Solution()
print(solve.intersect(nums1, nums2))
print(solve.intersect2(nums1, nums2))
