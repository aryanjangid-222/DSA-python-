class Solution(object):
    def isMiddleElementUnique(self, nums):
        m = len(nums)//2
        c = 0
        mid = nums[m]
        for el in nums:
            if el == mid:
                c += 1
        return c == 1
        