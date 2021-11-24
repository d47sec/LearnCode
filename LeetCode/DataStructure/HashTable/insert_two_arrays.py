class Solution:
    def intersection(self, nums1, nums2):
        hashSet1 = set(nums1)
        hashSet2 = set(nums2)
        
        if len(hashSet1) < len(hashSet2):
            return [x for x in hashSet1 if x in hashSet2]
        else:
            return [x for x in hashSet2 if x in hashSet1]
        

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

solve = Solution()
print(solve.intersection(nums1, nums2))
        
        
        