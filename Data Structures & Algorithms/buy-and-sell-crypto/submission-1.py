class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        p1,p2 = 0,1
        max_profit = 0

        while p2 < n:
            if prices[p1] > prices[p2]:
                p1 = p2
                p2 += 1
            else:
                max_profit = max(max_profit,prices[p2]-prices[p1])
                p2 += 1
        return max_profit