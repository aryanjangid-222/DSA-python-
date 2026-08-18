class Solution(object):
    def firstUniqChar(self, s):
        l = len(s)
        if l < 27:
            a = -1
            for i in s:
                a += 1
                if s.count(i)==1:
                    return a
            return -1
        char = "abcdefghijklmnopqrstuvwxyz"
        a = l
        for i in char:
            if s.count(i)==1:
                if s.find(i) < a:
                    a = s.find(i)
        if a != l:
            return a
        return -1
        