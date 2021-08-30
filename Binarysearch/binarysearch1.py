# DAY 3
from math import ceil
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while(l < r):
            mid = ceil((l + r)/2)
            if(mid * mid <= x):
                l = mid
            else:
                r = mid - 1
        return l

# leetcode sqrt()
# https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
