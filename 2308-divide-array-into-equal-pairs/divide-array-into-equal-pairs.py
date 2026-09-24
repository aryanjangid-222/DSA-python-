class Solution(object):
    def divideArray(self, nums):
        check = list(set(nums))
        for el in check:
            if nums.count(el) % 2:
                return False
        return True