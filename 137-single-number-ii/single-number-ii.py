class Solution(object):
    def singleNumber(self, nums):
        for el in nums:
            if nums.count(el) == 1:
                return el
            