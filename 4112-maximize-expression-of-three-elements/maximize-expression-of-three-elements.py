class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        nums.sort()
        l = len(nums)
        return nums[l-1]+nums[l-2]-nums[0]