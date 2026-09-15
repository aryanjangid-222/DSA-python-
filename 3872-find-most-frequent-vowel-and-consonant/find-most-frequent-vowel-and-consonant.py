class Solution(object):
    def maxFreqSum(self, s):
        max_freV = 0
        max_freC = 0
        org = list(set(s))
        vowal = "aeiou"
        for el in org:
            c = s.count(el)
            if el in vowal:
                if c > max_freV:
                    max_freV = c
                continue
            elif c > max_freC:
                max_freC = c
        
        return max_freV + max_freC
        