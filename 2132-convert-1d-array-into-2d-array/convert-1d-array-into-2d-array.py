class Solution(object):
    def construct2DArray(self, original, m, n):
        out = []
        if m*n != len(original):
            return []
        c = -1
        for j in range(m):
            li = []
            for i in range(n):
                c += 1
                li.append(original[c])
            out.append(li)
        
        return out