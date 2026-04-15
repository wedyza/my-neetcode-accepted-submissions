class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for i in range(n-1, 0, -1):
            sell_price = prices[i]
            buy_price = min(prices[:i])
            profit = max(sell_price - buy_price, profit)
        return profit