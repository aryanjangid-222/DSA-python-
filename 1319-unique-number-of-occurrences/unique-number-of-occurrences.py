class Solution(object):
    def uniqueOccurrences(self, arr):
        check = []
        c1 = list(set(arr))
        for el in c1:
            c = arr.count(el)
            if c in check:
                return False
            check.append(c)
        return True
        