from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dick = Counter(s)
        size = 0
        od = 0
        for i in dick.values():
            if i%2 == 0:
                size+=i
            else:
                if i == 1 and od==0:
                    od = 1
                    size+=i
                elif i != 1 and od == 0:
                    size+=i
                    od = 1
                elif i!=1 and od == 1:
                    size+=(i-1)
        return size