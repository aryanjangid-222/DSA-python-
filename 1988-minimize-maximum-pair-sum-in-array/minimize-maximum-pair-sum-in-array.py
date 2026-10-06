class Solution(object):
    def minPairSum(self, nums):
        check = sorted(nums)
        res = 0
        l = len(check)
        for i in range(l/2):
            s = check[i] + check[-(1+i)]
            if s > res:
                res = s
        return res