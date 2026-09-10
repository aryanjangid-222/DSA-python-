class Solution(object):
    def maximumCount(self, nums):
        n = 0
        p = 0 
        for el in nums:
            if el < 0:
                n += 1
            elif el > 0:
                p += 1
        
        return p if p > n else n