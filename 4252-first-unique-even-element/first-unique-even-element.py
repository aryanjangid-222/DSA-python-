class Solution(object):
    def firstUniqueEven(self, nums):
        for el in nums:
            if el % 2 == 0 and nums.count(el) == 1:
                return el
        return -1