class Solution(object):
    def prefixCount(self, words, pref):
        l = len(pref)
        res = 0
        for el in words:
            if el[:l] == pref:
                res += 1
        return res