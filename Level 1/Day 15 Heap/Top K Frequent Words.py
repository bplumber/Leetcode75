class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dick = dict(Counter(words))
        dick1 = {}
        sorted_keys = sorted(dick, key=dick.get, reverse = True)  
        for w in sorted_keys:
            dick1[w] = dick[w]
        dick3 = {}
        for x, v in dick1.items():
            if v in dick3:
                dick3[v].append(x)
            else:
                dick3[v] = [x]
        for x,v in dick3.items():
            temp = v
            temp.sort()
            dick3[x] = temp
        rt = []
        for x,v in dick3.items():
            rt.append(v)
        rt = sum(rt, [])
        return rt[:k]
        