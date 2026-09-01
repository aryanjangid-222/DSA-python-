class Solution(object):
    def pivotIndex(self, nums):
        s = sum(nums)
        s1 = 0
        for i in range(len(nums)):
            s -= nums[i]
            if s1==s:
                return i
            s1 += nums[i]
        return -1
        