class Solution(object):
    def finalPrices(self, prices):
        out = []
        for i in range(len(prices)):
            diss = True
            e = prices[i]
            for j in range(i+1,len(prices)):
                if prices[j] <= e:
                    out.append(e - prices[j])
                    diss = False
                    break
            if diss:
                out.append(e)
        
        return out
        