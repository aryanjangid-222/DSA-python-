class Solution(object):
    def findDuplicate(self, nums):
        a = nums
        a.sort()
        for i in range(len(a)-1):
            if a[i]==a[i+1]:
                return a[i]
        