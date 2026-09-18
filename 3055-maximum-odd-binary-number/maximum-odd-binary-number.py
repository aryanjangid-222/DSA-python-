class Solution(object):
    def maximumOddBinaryNumber(self, s):
        l = len(s)
        c = s.count("1")
        li = ["0"]*l
        i = 0
        while i != c-1:
            li[i] = "1"
            i += 1
        li[l-1] = "1"
        return "".join(map(str,li))
        