def merge(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    l = n + m - 1
    result = [0] * (n+m)
    while n > 0 and m > 0:
        if nums1[n-1] > nums2[m-1]:
            result[l] = nums1[n-1]
            l -= 1
            n -= 1
        else:
            result[l] = nums2[m-1]
            l -= 1
            m -= 1
    while n > 0:
        result[n-1] = nums1[n-1]
        n-=1
    while m > 0:
        result[m-1] = nums2[m-1]
        m-=1
    return result            
    
nums1 = [1,2,3,4]
nums2 = [1,3,9]
print(merge(nums1, nums2))
