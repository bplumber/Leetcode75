class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                if prices[r] - prices[l] > mx:
                    mx = prices[r]-prices[l]
            r+=1
        return mx