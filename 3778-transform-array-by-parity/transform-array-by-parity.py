class Solution(object):
    def transformArray(self, nums):
        out = []
        for el in nums:
            if el % 2 == 0:
                out.insert(0,0)
                continue
            out.append(1)
        
        return out
        