# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        # while l <= r:
        #     m = (r + l) // 2
        #     if isBadVersion(m) == True:
        #         r = m - 1
        #     if isBadVersion(m) == False:
        #         l = m + 1
        #     if l > r:
        #         return l
        i=0
        while l <= r:
            m = (r + l) // 2
            if isBadVersion(m):
                r = m - 1
                i = m
            else:
                l = m + 1
        return i