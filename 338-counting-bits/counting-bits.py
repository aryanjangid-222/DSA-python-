class Solution(object):
    def countBits(self, n):
        res = []
        for i in range(n + 1):
            n = 0
            while i != 0:
                if i % 2:
                    i -= 1
                    n += 1
                else:
                    i /= 2
            res.append(n)
        return res