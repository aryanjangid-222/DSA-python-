class Solution(object):
    def runningSum(self, nums):
        out = []
        s = 0
        for el in nums:
            s += el
            out.append(s)
        return out
        