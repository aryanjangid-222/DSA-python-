class Solution(object):
    def twoSum(self, nums, target):
        a = -1
        b = -1
        for i in nums:
            a += 1
            b = -1
            for j in nums:
                b += 1
                if (a==b):
                    break
                if (i+j)==target:
                    return [a, b]
        
        