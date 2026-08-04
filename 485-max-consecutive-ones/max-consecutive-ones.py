class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if nums==0:
            return 0
        a = 0
        m = 0
        for el in nums:
            if 1 == el:
                a += 1
            else:
                if a>m:
                    m = a
                a = 0
        if a>m:
            return a
        else:
            return m
        