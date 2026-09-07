class Solution(object):
    def maximumDifference(self, nums):
        l = len(nums)
        m = -1
        mi = max(nums)
        for i in range(l-1):
            mi = min(mi,nums[i])
            diff = nums[i+1] - mi
            m = max(m,diff)
        
        return m if m > 0 else -1