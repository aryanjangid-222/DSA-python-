class Solution(object):
    def intersection(self, nums):
        out = []
        past = []
        a = 0
        for el in nums:
            if a==0:
                past = el
                a = 1
                continue
            for i in past:
                if i in el:
                    out.append(i)
                    el.remove(i)
            past = out
            if out == []:
                return out
            out = []
        past.sort()
        return past