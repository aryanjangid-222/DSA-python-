class Solution(object):
    def sortArrayByParityII(self, nums):
        even = []
        odd = []
        out = []
        for el in nums:
            if el%2==0:
                even.append(el)
            else:
                odd.append(el)
        for i in range(len(even)):
            out.append(even[i])
            out.append(odd[i])
        return out