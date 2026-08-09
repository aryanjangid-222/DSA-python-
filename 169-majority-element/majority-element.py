class Solution(object):
    def majorityElement(self, nums):
        l = len(nums)
        if l>100:
            for el in nums[::-1]:
                if nums.count(el)>l/2:
                    return el
        for el in nums:
            if nums.count(el)>l/2:
                return el
         