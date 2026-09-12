class Solution(object):
    def pivotArray(self, nums, pivot):
        out = []
        for el in nums:
            if el < pivot :
                out.append(el)
        
        for i in range(nums.count(pivot)):
            out.append(pivot)
        
        for el in nums:
            if el > pivot:
                out.append(el) 
               
        return out