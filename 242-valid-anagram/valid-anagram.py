class Solution(object):
    def isAnagram(self, s, t):
        c = "abcdefghijklmnopqrstuvwxyz"
        for i in c:
            if s.count(i)!=t.count(i):
                return False
        return True