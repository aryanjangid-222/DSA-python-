class Solution(object):
    def findLucky(self, arr):
        ch = list(set(arr))
        for el in ch[::-1]:
            if arr.count(el)==el:
                return el
        return -1