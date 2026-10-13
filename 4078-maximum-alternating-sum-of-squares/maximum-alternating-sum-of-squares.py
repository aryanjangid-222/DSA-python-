class Solution(object):
    def maxAlternatingSum(self, nums):
        check = [el*el for el in nums]
        check.sort()
        l = len(check)
        return sum(check[l/2:]) - sum(check[:l/2])