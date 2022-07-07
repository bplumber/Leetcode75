class Solution:
    def climbStairs(self, n: int) -> int:
        # ct = 0
        # def hlp(stp, left):
        #     nonlocal ct
        #     if left < 0:
        #         return 
        #     if left == n:
        #         ct+=1
        #         return
        #     hlp(stp-1, left-1)
        #     hlp(stp-2, left-2)
        # hlp(n,n)
        # return ct
        one = 1
        two = 1
        temp = 1
        for i in range(n-1):
            temp = one+two
            two = one
            one = temp 
        return temp