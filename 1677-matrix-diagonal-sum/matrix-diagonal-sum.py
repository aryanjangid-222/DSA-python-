class Solution(object):
    def diagonalSum(self, mat):
        first = 0
        last = len(mat[0])-1
        s = 0
        for el in mat:
            s += el[first] + el[last]
            if first == last:
                s -= el[first]
            first += 1
            last -= 1
        
        return s