class Solution(object):
    def sumOfUnique(self, nums):
        s = 0
        for el in nums:
            if nums.count(el)==1:
                s += el
        return s