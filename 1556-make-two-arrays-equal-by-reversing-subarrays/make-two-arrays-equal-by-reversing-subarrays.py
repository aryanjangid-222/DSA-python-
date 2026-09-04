class Solution(object):
    def canBeEqual(self, target, arr):
        for el in target:
            if target.count(el) == arr.count(el):
                continue
            else:
                return False
        return True