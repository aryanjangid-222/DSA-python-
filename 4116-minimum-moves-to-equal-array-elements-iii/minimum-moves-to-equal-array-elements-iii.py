class Solution(object):
    def minMoves(self, nums):
        nums.sort()
        m = nums[len(nums)-1]
        res = 0
        for el in nums:
            res += m-el
        return res