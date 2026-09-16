class Solution(object):
    def maxFreqSum(self, s):
        li = list(set(s))
        check = "aeiou"
        max_freV = 0
        max_freC = 0
        for el in li:
            c = s.count(el)
            if el in check:
                if c > max_freV:
                    max_freV = c
            elif max_freC < c:
                max_freC = c
        
        return max_freC + max_freV
