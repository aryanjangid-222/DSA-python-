class Solution(object):
    def averageValue(self, nums):
        check = []
        for el in nums:
            if el % 6 == 0:
                check.append(el)
        
        s = sum(check)
        l = len(check)
        return s/l if l != 0 else 0
        