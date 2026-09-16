class Solution(object):
    def removeDuplicates(self, nums):
        li = list(set(nums))
        li.sort()
        out = []
        for el in li:
            out.append(el)
            if nums.count(el)>1:
                out.append(el)
        l = len(out)
        for i in range(l):
            nums[i] = out[i]
        return l