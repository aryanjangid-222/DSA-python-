class Solution(object):
    def repeatedNTimes(self, nums):
        n = len(nums)/2
        for el in nums:
            if nums.count(el)==n:
                return el
        