class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        out = []
        for el in nums:
            a = 0
            for el1 in nums:
                if el1<el:
                    a += 1
            out.append(a)
        return out
