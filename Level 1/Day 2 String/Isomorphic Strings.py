class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dick = {}
        for i,j in zip(s,t):
            if i not in dick and j not in list(dick.values()):
                dick[i]=j
        for i,j in zip(s,t):
            if i not in dick:
                return False
            if dick[i]!=j:
                return False
        return True