class Solution(object):
    def missingMultiple(self, nums, k):
        for i in range(1,len(nums)+2):
            if nums.count(i*k)==0:
                return i*k
            