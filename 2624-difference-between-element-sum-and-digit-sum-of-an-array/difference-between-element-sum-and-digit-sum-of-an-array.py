class Solution(object):
    def differenceOfSum(self, nums):
        s = 0 
        ds = 0
        for el in nums:
            s += el
            while el != 0:
                    ds += el % 10
                    el //= 10
        
        return s - ds   