class Solution(object):
    def findLucky(self, arr):
        ch = list(set(arr))
        a = -1
        for el in ch:
            if arr.count(el)==el:
                a = el
        return a