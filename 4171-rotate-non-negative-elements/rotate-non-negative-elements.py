class Solution(object):
    def rotateElements(self, nums, k):
        if k==0:
            return nums
        l = len(nums)
        pos = []
        res = ["."]*l
        for i,el in enumerate(nums):
            if el < 0:
                res[i] = el
            else:
                pos.append(el)
        len_pos = len(pos)
        if len_pos == 0:
            return nums
        j = k % len_pos
        for i in range(l):
            if res[i] == ".":
                res[i] = pos[j]
                j += 1
                if j == len_pos:
                    j = 0
        return res