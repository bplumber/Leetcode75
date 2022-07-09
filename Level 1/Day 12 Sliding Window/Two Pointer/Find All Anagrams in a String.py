class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        x = dict(Counter(p))
        lt = []
        i = 0
        j = len(p)-1
        while i < (len(s)-len(p)+1):
            if s[j] in p:
                temp = dict(Counter(s[i:j+1]))
                if temp == x:
                    lt.append(i)
                i+=1
                j+=1
            else:
                i = j+1
                j =i + len(p) -1
        return lt