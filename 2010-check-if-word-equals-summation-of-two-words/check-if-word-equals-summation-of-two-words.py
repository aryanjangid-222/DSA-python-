class Solution(object):
    def isSumEqual(self, f, s, t):
        char = "abcdefghij"
        i = 0
        ii = 0
        iii = 0
        for ind in range(8):
            if ind < len(f):
                i = i*10 + char.index(f[ind])
            if ind < len(s):
                ii = ii*10 + char.index(s[ind])
            if ind < len(t):
                iii = iii*10 + char.index(t[ind])

        return i + ii == iii 