class Solution(object):
    def sortArray(self, nums):
        mi = min(nums)
        ma = max(nums)
        res = []
        count = [0] * (ma-mi + 1)
        for el in nums:
            count[el - mi] += 1
        for i in range(len(count)):
            res += [i + mi] * count[i]
        return res