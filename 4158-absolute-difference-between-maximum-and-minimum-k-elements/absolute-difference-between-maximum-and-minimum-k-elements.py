class Solution(object):
    def absDifference(self, nums, k):
        l = len(nums)
        if l==1:
            return 0
        nums.sort()
        s1 = 0
        s2 = 0
        for i in range(k):
            s2 += nums[i]
            s1 += nums[l-1-i]
        return s1-s2