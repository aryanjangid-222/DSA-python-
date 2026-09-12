class Solution(object):
    def findClosestNumber(self, nums):
        nums.sort()
        res = 0
        pre = 0
        el = nums[0]
        i = 0
        if nums[len(nums) - 1] < 0:
            return nums[len(nums) - 1]
        elif el > 0:
            return el
        while el < 0:
            i += 1
            pre = el
            el = nums[i]

        return pre if abs(pre) < el else el