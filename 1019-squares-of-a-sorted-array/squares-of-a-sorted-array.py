class Solution(object):
    def sortedSquares(self, nums):
        out = []
        for el in nums:
            out.append(el**2)
        out.sort()
        return out