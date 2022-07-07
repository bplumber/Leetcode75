class Solution:
    def fib(self, n: int) -> int:
#         def hlp(n):
#             if n == 0:
#                 return 0
#             if n == 1:
#                 return 1
#             return hlp(n-1)+hlp(n-2)
        
#         return hlp(n)
        lt = [0,1]
        for i in range(2, n+1):
            lt.append(lt[i-1]+lt[i-2])
        return lt[n]