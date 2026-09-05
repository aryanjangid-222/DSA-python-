class Solution(object):
    def replaceElements(self, arr):
        m = -1
        l = len(arr)
        for i in range(-1,-l-1,-1):
            el = arr[i]
            arr[i] = m
            if m < el:
                m = el
        return arr