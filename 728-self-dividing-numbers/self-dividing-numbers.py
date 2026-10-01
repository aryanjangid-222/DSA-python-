class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []
        for i in range(left,right + 1):
            if i < 10:
                res.append(i)
                continue
            c = True
            for j in str(i):
                if j == "0":
                    c = False
                    break
                if i % int(j) != 0:
                    c = False
                    break
            if c:
                res.append(i)
        return res
        