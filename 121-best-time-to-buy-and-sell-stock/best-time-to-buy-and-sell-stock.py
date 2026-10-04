class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        min_price = prices[0]
        max_profit = prices[1] - prices[0]
        for el in prices:
            if el < min_price:
                min_price = el
            elif el - min_price > max_profit:
                max_profit = el - min_price
        return max_profit