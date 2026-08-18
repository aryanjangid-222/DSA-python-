class Solution(object):
    def dominantIndex(self, nums):
        max = 0
        a = 0
        for i in nums:
            if i > max:
                a = max
                max = i
            elif i > a:
                a = i
        if 2*a <= max:
            return nums.index(max)
        else:
            return -1