<<<<<<< HEAD
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while(l <= r):
            mid = (l + r) // 2
            if(isBadVersion(mid)):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
=======
# DAY 4
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while(l <= r):
            mid = (l + r) // 2
            if(isBadVersion(mid)):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
>>>>>>> 5bf1aca1b0b9ded29bfd67fa46a4c108330edd7a
