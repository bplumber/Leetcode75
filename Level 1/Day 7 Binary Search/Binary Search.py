class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        found = False
        while l<=r:
            mid = l +(r-l)//2
            if nums[mid]==target:
                found = True
                break
            elif nums[mid]> target:
                r = mid - 1
            elif target > nums[mid]:
                l = mid+ 1
        if found:
            return mid
        else:
            return -1