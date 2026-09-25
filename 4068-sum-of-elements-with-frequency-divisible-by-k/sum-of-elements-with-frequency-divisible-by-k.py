class Solution(object):
    def sumDivisibleByK(self, nums, k):
        s = 0
        check = list(set(nums))
        for el in check:
            c = nums.count(el)
            if c % k == 0:
                s += el * c
        return s