class Solution(object):
    def kthDistinct(self, arr, k):
        out = []
        for el in arr:
            if arr.count(el)==1:
                out.append(el)
        if k>len(out):
            return ""
        return out[k-1]