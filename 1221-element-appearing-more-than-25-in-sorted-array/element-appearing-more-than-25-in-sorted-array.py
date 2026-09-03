class Solution(object):
    def findSpecialInteger(self, arr):
        l = len(arr)
        for i in range(l):
            if arr[i] == arr[i + l//4]:
                return arr[i]