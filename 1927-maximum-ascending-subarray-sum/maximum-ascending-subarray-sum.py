class Solution(object):
    def maxAscendingSum(self, nums):
        s1 = nums[0]
        s2 = 0
        l = len(nums)
        for i in range(l-1):
            if nums[i] < nums[i+1]:
                s1 += nums[i+1]
            else:
                if s1 > s2:
                    s2 = s1
                s1 = nums[i+1]
        if s1 > s2:
            return s1
        return s2