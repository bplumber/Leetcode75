class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p = []
        for i in range(len(nums)):
            if i==0:
                p.append(nums[i])
            else:
                p.append(p[i-1]+nums[i])
        rt = -1
        for i in range(len(p)):
            if p[i] - nums[i] == p[len(p)-1] - p[i]:    
                return i
        return rt
    