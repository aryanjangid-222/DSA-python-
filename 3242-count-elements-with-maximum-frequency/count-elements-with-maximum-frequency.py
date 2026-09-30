class Solution(object):
    def maxFrequencyElements(self, nums):
        check = []
        li = list(set(nums))
        if len(li) == len(nums):
            return len(nums)
        for el in li:
            check.append(nums.count(el))
        m = max(check)
        return m * check.count(m)
        