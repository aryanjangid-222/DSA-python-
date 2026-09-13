class Solution(object):
    def maxAdjacentDistance(self, nums):
        l = len(nums)
        m = abs(nums[0]-nums[l-1])
        for i in range(l-1):
            d = abs(nums[i]-nums[i+1])
            if d > m:
                m = d
        
        return m