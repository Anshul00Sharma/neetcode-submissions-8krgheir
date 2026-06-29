class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur = float('inf')
        for p in prices:
            if p < cur:
                cur = p
            profit = max(profit, p - cur)
        return int(profit)