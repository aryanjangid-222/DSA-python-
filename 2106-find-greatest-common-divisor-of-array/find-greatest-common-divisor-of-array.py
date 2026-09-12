class Solution(object):
    def findGCD(self, nums):
        max_num = max(nums)
        min_num = min(nums)
        res = 1
        for i in range(min_num,1,-1):
            if min_num % i == 0 and max_num % i == 0:
                res = i
                break
        
        return res