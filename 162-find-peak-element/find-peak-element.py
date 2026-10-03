class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        return nums.index(max(nums))