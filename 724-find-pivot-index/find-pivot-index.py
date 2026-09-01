class Solution(object):
    def pivotIndex(self, nums):
        s = 0
        s1 = 0
        for el in nums:
            s += el

        for i in range(len(nums)):
            s -= nums[i]
            if s1==s:
                return i
            s1 += nums[i]
        return -1
        