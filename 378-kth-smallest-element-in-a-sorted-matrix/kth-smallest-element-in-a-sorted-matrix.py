class Solution(object):
    def kthSmallest(self, matrix, k):
        check = []
        for el in matrix:
            for i in el:
                check.append(i)
        check.sort()
        return check[k-1]