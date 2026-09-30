class Solution(object):
    def maxFrequencyElements(self, nums):
        li = list(set(nums))
        if len(li) == len(nums):
            return len(nums)
        ma = 0
        coun = 0
        for el in li:
            c = nums.count(el)
            if c > ma:
                ma = c
                coun = 1
            elif c == ma:
                coun += 1
        return ma * coun        