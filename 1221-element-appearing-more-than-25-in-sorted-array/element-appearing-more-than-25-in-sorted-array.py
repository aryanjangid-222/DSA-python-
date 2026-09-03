class Solution(object):
    def findSpecialInteger(self, arr):
        l = len(arr)
        li = list(set(arr))
        for el in li:
            if arr.count(el) > l//4:
                return el 