# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        upper = n
        lower = 0
        mid = int((upper+lower)/2)
        while True:
            if isBadVersion(mid):
                upper = mid
                mid = int((upper+lower)/2)
            else:
                lower = mid
                mid = int((upper+lower)/2)
            if upper - lower <= 1:
                return upper
        """
        :type n: int
        :rtype: int
        """
