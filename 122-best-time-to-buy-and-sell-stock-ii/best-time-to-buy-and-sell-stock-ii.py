class Solution(object):
    def maxProfit(self, prices):
        res = 0
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i] > prices[i+1]:
                res += max_profit
                max_profit = 0
            elif prices[i] < prices[i+1]:
                max_profit += prices[i+1] - prices[i]  
        
        return res + max_profit