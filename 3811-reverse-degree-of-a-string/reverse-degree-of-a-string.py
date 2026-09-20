class Solution(object):
    def reverseDegree(self, s):
        a = "1zyxwvutsrqponmlkjihgfedcba"
        su = 0
        i = 0
        for el in s:
            i += 1
            su += a.index(el)*i
        return su