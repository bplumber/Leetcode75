class Solution:
    def decodeString(self, s: str) -> str:
        x = ""
        rt = []
        for i in s:
            if i != ']':
                rt.append(i)
            else:
                temp = ""
                while rt[-1]!='[':
                    temp = str(rt.pop()) + temp
                rt.pop()
                n = ""
                while rt and rt[-1].isdigit():
                    n = rt.pop() + n
                n = int(n)
                rt.append(n*temp)
        return ''.join(rt)