class Solution(object):
    def construct2DArray(self, original, m, n):
        out = []
        if m*n != len(original):
            return []
        curr = 0
        nex = n
        for i in range(m):
            out.append(original[curr:nex])
            curr += n
            nex += n
        return out

        return out