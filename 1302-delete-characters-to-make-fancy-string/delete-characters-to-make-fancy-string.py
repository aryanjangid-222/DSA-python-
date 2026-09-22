class Solution(object):
    def makeFancyString(self, s):
        if len(s) < 3:
            return s
        l = len(s)
        res = ""
        for i in range(l-2):
            if s[i] == s[i+1] and s[i] == s[i+2]:
                continue
            res += s[i]
        
        res += s[l-2] + s[l-1]
        return res