class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        equal_el = nums[len(nums)//2]
        res = 0
        for el in nums:
            res += abs(el-equal_el)
        return res