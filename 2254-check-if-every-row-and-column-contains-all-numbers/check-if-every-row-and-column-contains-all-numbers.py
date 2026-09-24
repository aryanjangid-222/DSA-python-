class Solution(object):
    def checkValid(self, matrix):
        l = len(matrix[0])
        for el in matrix:
            num = range(1,l+1)
            for i in range(l):
                if el[i] in num:
                    num.remove(el[i])
                else:
                    return False
            
        for i in range(l):
            num = range(1,l+1)
            for el in matrix:
                if el[i] in num:
                    num.remove(el[i])
                else:
                    return False
        
        return True