class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr1.sort()
        out = []
        for el in arr2:
            if el in arr1:
                c = arr1.count(el)
                for i in range(c):
                    out.append(el)
                    arr1.remove(el)
        return out + arr1