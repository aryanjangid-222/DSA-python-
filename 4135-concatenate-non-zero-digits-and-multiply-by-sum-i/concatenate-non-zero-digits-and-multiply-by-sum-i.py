class Solution(object):
    def sumAndMultiply(self, n):
        if n == 0:
            return 0
        s = 0
        num = ""
        for el in str(n):
            if el != "0":
                num += el
                s += int(el)

        return int(num) * s
