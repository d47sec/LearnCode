# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        # result = 0
        while l < r:
            mid = int((l+r)/2)
            if isBadVersion(mid):
                r  = mid
            else:
                l = mid + 1
        return l