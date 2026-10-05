class Solution(object):
    def singleNonDuplicate(self, nums):
        l = len(nums)
        if l == 1:
            return nums[0]
        for i in range(0,l-1,2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[l-1]