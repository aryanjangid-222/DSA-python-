class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for el in nums:
            a ^= el
        return a