class Solution(object):
    def maximumGap(self, nums):
        if len(nums)==1:
            return 0
        nums.sort()
        l = len(nums)
        a = 0
        for i in range(l-1):
            if nums[i+1]-nums[i]>a:
                a = nums[i+1]-nums[i]
        return a