class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for i in s:
            if i == '#' and len(s1)!=0:
                s1.pop()
            elif i!='#':
                s1.append(i)
        for i in t:
            if i == '#' and len(s2)!=0:
                s2.pop()
            elif i!='#':
                s2.append(i)
        return s1==s2