class Solution(object):
    def singleNumber(self, nums):
        out = []
        for el in nums:
            if el in out:
                out.remove(el)
            else:
                out.append(el)
        return out
        