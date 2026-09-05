class Solution(object):
    def checkIfExist(self, arr):
        if arr.count(0) > 1:
            return True
        for el in arr:
            if 2*el in arr and el != 0:
                return True
        else:
            return False