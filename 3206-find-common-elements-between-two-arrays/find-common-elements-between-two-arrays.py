class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        ans1 = 0
        ans2 = 0
        for el in nums1:
            if el in nums2:
                ans1 += 1
        for el in nums2:
            if el in nums1:
                ans2 += 1
        return [ans1,ans2]