class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        res = []
        for el in nums1:
            if el in res:
                continue
            if el in nums2:
                res.append(el)
            elif el in nums3:
                res.append(el)
        
        for el in nums2:
            if el in res:
                continue
            if el in nums3:
                res.append(el)
        
        return res
        