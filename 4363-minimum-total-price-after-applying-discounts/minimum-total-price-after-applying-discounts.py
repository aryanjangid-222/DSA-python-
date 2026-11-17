class Solution(object):
    def minPrice(self, prices, discounts):
        prices.sort(reverse = True)
        discounts.sort(reverse = True)
        res = sum(prices)
        l = len(prices)
        if l > len(discounts):
            l = len(discounts)
        for i in range(l):
            res -= prices[i] * discounts[i] / 100.0
        
        return res