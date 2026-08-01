class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n <= 1:
            return 0

        buy = 0
        sell = 1
        profit = 0

        while sell < n:

            if prices[buy] > prices[sell]:
                buy = sell

            profit = max(profit, prices[sell] - prices[buy])
            sell += 1

        return profit