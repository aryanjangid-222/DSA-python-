class Solution(object):
    def leftRightDifference(self, nums):
        right = sum(nums)
        left = 0
        out = []
        for el in nums:
            right -= el
            out.append(abs(right - left))
            left += el

        return out