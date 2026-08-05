class Solution(object):
    def searchInsert(self, nums, target):
        a = -1
        for el in nums:
            a += 1
            if el==target:
                return a
            if target<el:
                return a
        return a+1
        