class Solution(object):
    def isMiddleElementUnique(self, nums):
        mid = nums[len(nums)//2]
        return nums.count(mid) == 1
        