class Solution(object):
    def optimalDivision(self, nums):
        l = len(nums)
        if l == 1:
            return str(nums[0])
        res = "/".join(map(str,nums))
        if l > 2:
            res += ')'
            res = res.replace("/","/(",1)
        return res

        