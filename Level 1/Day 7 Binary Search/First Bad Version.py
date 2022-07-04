# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1) == True:
            return 1
        l = 0
        r = n
        while l <= r:
            mid = l + (r-l)//2
            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            elif isBadVersion(mid) == True and isBadVersion(mid-1) == True:
                r = mid - 1
            elif isBadVersion(mid) == False:
                l = mid + 1
        