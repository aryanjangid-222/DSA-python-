class Solution(object):
    def reverseWords(self, s):
        s1 = s.split()
        s2 = s1[::-1]
        return " ".join(map(str,s2))
        