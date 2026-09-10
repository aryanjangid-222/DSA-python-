class Solution(object):
    def maximizeSum(self, nums, k):
        nums.sort()
        el = nums[len(nums)-1]
        s = 0
        for i in range(k):
            s += el
            el += 1
        
        return s