class Solution(object):
    def addToArrayForm(self, num, k):
        n = 0
        for el in num:
            n = n*10 + el
        s = n + k
        out = []
        while s != 0:
            out.append(s%10)
            s = s//10
        return out[::-1]