class Solution(object):
    def intersection(self, nums1, nums2):
        out = []
        for el in nums1:
            for el_1 in nums2:
                if el == el_1:
                    out.append(el)
        return list(set(out))
        