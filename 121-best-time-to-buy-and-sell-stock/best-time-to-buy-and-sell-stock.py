class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0

        if len(prices) <= 1:
            return 0
        else:
            sell = 1
            profit = prices[sell] - prices[buy] 

        while (sell <= (len(prices) - 1)):

            if prices[buy] > prices[sell]:
                buy = sell

            profit = max(profit, prices[sell] - prices[buy])
            sell += 1

        return profit