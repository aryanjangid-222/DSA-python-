class Solution(object):
    def reverseDegree(self, s):
        a = "1zyxwvutsrqponmlkjihgfedcba"
        su = 0
        for i in range(len(s)):
            su += a.index(s[i])*(i+1)
        return su