class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(m,n+m):
            nums1[i]=nums2[i-m]
        nums1.sort()
        