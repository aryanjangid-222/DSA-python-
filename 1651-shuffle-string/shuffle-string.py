class Solution(object):
    def restoreString(self, s, indices):
        out=[]
        a = 0
        for i in range(len(s)):
            out.append("")
        for el in indices:
            out[el]=s[a]
            a += 1
        return "".join(map(str,out))
        