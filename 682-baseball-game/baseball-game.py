class Solution(object):
    def calPoints(self, nums):
        res = []
        l = len(nums)
        i = -1
        c = -1
        while i !=  l-1:
            i += 1
            if nums[i] == "+":
                res.append(res[c]+res[c-1])
                c += 1
            elif nums[i] == "D":
                res.append(2*res[c])
                c += 1
            elif nums[i] == "C":
                res.remove(res[c])
                c = len(res)-1
            else:
                res.append(int(nums[i]))
                c += 1
        sum = 0
        for el in res:
            sum += el
        return sum