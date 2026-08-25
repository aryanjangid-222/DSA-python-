class Solution(object):
    def repeatedNTimes(self, nums):
        n = len(nums)/2
        num = list(set(nums))
        for el in num:
            if nums.count(el)==n:
                return el
        