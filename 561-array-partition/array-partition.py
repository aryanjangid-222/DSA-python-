class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        l = len(nums)
        s = 0
        for i in range(0,l,2):
            s += nums[i]
        return s
        