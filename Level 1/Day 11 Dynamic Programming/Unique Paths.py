class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ct = 0
        # def hlp(r, c):
        #     nonlocal ct 
        #     if r >= m or c >= n: 
        #         return 
        #     if r == m-1 and c == n - 1:
        #         ct+=1
        #         return
        #     hlp(r+1, c)
        #     hlp(r, c+1)
        # hlp(0,0)
        # return ct
        lt = [[0]*(n+1)]*(m+1)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    lt[i][j]=1
                else:
                    lt[i][j] = lt[i-1][j] + lt [i][j-1]
        return lt[m][n]
        
        
        
        
        