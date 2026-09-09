class Solution(object):
    def mostFrequentEven(self, nums):
        check = list(set(nums))
        check.sort()
        m = 0
        res = -1
        for el in check:
            if el % 2 != 0:
                continue
            c = nums.count(el)
            if c > m:
                m = c
                res = el
        return res