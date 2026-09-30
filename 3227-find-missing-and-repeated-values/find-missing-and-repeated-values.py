class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        check = []
        l =len(grid)
        res = [0,0]
        rep = True
        for li in grid:
            for el in li:
                if rep:
                    if el in check:
                        res[0] = el
                        rep = False
                check.append(el)
        for i in range(1,(l**2) + 1):
            if i in check:
                continue
            else:
                res[1] = i
                return res
        