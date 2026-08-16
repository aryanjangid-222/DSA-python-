class Solution(object):
    def intersect(self, nums1, nums2):
        out = []
        for el in nums1:
            if el in nums2:
                out.append(el)
                nums2.remove(el)
        return out