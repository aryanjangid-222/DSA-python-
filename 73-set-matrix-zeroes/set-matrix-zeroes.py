class Solution(object):
    def setZeroes(self, matrix):
        check = []
        l = len(matrix)
        lm = len(matrix[0])
        for i in range(l):
            iszero = False
            for j in range(lm):
                if matrix[i][j] == 0:
                    iszero = True
                    check.append(j)
            if iszero:
                for k in range(lm):
                    matrix[i][k] = 0
        check = list(set(check))
        for el in check:
            for i in range(l):
                matrix[i][el] = 0