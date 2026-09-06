class Solution(object):
    def finalPrices(self, prices):
        out = []
        for i in range(len(prices)):
            e = prices[i]
            el = 0
            for j in range(i+1,len(prices)):
                if prices[j] <= e:
                    el = prices[j]
                    break
            
            out.append(e - el)
        
        return out
        