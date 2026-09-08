class Solution(object):
    def maximumWealth(self, accounts):
        m = 0
        for el in accounts:
            s = sum(el)
            if s > m:
                m = s
        
        return m
