class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a = sorted(nums1 + nums2)
        b = len(a)
        if b%2==0:
            return (a[b/2]+a[(b/2)-1])/2.0
        else:
            return a[(b//2)]

        