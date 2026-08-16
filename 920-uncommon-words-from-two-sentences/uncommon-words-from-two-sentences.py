class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        out = []
        s = s1 + " " + s2
        s = s.split()
        for el in s:
            if s.count(el)==1:
                out.append(el)
        return out