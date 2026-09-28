class Solution(object):
    def customSortString(self, order, s):
        res = ""
        for el in order:
            if el in s:
                res += el*s.count(el)
                s = s.replace(el,"")
        return res + s