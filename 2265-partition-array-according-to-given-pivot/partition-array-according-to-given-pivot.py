class Solution(object):
    def pivotArray(self, nums, pivot):
        first = []
        second = []
        third = []
        for el in nums:
            if el < pivot :
                first.append(el)
                continue
            elif el == pivot:
                second.append(el)
                continue
            else:
                third.append(el)
        
        return first + second + third    