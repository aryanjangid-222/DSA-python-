class Solution(object):
    def getKth(self, lo, hi, k):
        check = []
        elem = []
        for el in range(lo,hi+1):
            p = 0
            elem.append(el)
            while el != 1:
                if el % 2:
                    p += 1
                    el = el*3 + 1
                else:
                    p += 1
                    el /= 2
            check.append(p)
        fir,out = zip(*sorted(zip(check, elem)))
        return out[k-1]