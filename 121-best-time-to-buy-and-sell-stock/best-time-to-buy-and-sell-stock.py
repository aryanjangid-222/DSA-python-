class Solution(object):
    def maxProfit(self, prices):
        mi1 = prices[0]
        ind = 0
        for i,el in enumerate(prices):
            if el < mi1:
                mi1 = el
                ind = i
        ma1 = max(prices[ind:])
        res1 = ma1 - mi1
        check = prices[0:ind]
        l = len(check)
        res2 = 0
        for i in range(l):
            res = max(check[i:]) - check[i]
            if res > res2:
                res2 = res
        return res1 if res1 > res2 else res2