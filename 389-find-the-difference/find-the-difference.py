class Solution(object):
    def findTheDifference(self, s, t):
        char = "abcdefghijklmnopqrstuvwxyz"
        for i in char:
            if s.count(i)!=t.count(i):
                return i 