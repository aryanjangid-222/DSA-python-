class Solution(object):
    def maximumDifference(self, nums):
        l = len(nums)
        m = -1
        for i in range(l-1):
            for j in range(i+1,l):
                d = nums[j] - nums[i]
                if m < d and d != 0:
                    m = d

        return m