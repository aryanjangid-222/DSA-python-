class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        res = [""]* numRows
        ind = 0
        l = len(s)
        i = 0
        down = True
        up = False
        while ind != l:
            res[i] += s[ind]
            ind += 1
            if down:
                if i == numRows - 1:
                    i -= 1
                    down = False
                    up = True
                else:
                    i += 1
            else:
                if i == 0:
                    i += 1
                    up = False
                    down = True
                else:
                    i -= 1
        
        out = ''
        for el in res:
            out += el
        return out