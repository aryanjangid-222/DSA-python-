class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        check = nums
        for el in check:
            if el == val:
                continue
            nums[i] = el
            i += 1
        return i