class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        brute-force solution: go through every single price, check the prices in the
        later days to see whether it would give us the maximum comparing to the current
        maximum we have, if yes then we replace that maximum. do it until we reach end
        of array. -> O(n^2)
        '''

        n = len(prices)

        maxProfit = 0
        minCost = prices[0]

        for i in range(n):
            minCost = min(minCost, prices[i])
            temp = prices[i] - minCost
            if temp > maxProfit:
                maxProfit = temp

        return maxProfit