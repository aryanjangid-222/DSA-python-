class Solution(object):
    def diStringMatch(self, s):
        d = len(s)
        i = 0
        out = []
        c = ""
        for el in s:
            if el == "D":
                out.append(d)
                d -= 1
                c = el
            else:
                out.append(i)
                i += 1
                c = el
        if c == "I":
            out.append(i)
            return out
        
        out.append(d)
        return out