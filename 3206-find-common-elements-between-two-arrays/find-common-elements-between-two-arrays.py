class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        num1 = list(set(nums1))
        num2 = list(set(nums2))
        first = 0
        second = 0
        for el in nums1:
            if el in num2:
                first += 1
        for el in nums2:
            if el in num1:
                second += 1
        return [first, second]