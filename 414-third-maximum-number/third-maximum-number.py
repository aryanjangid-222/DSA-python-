class Solution(object):
    def thirdMax(self, nums):
        nums_1 = list(set(nums))
        nums_1.sort()
        if len(nums_1)<3:
            return nums_1[len(nums_1)-1]
        return nums_1[len(nums_1)-3]
        