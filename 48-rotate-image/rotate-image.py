class Solution(object):
    def rotate(self, matrix):
        check = [el for el in matrix][::-1]
        l = len(check)
        for i in range(l):
            res = []
            for el in check:
                res.append(el[i])
            matrix[i] = res