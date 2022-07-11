class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dick = {}
        rt = 0
        l = 0
        for r in range(len(s)):
            dick[s[r]] = 1 + dick.get(s[r], 0)
            while (r-l+1) - max(dick.values())>k:
                dick[s[l]]-=1
                l+=1
            rt = max(rt, r-l+1)
        
        return rt