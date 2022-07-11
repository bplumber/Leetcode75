from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = []
        g = []
        for i,j in zip(secret, guess):
            s.append(i)
            g.append(j)
        bull = 0
        for i in range(len(s)):
            if s[i]==g[i]:
                s[i] = 'x'
                g[i] = 'x'
                bull+=1
        sd = Counter(s)
        tp = 0
        for i in g:
            if i in sd and i!='x':
                if sd[i]>0:
                    sd[i]-=1
                    tp+=1           
        return str(bull)+"A"+str(tp)+"B"