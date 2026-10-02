class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ma = 0
        seen = []
        for el in s:
            if el in seen:
                l = len(seen)
                if l > ma:
                    ma = l
                seen = seen[seen.index(el) + 1:l]
                seen.append(el)
            else:
                seen.append(el)
        
        return ma if ma > len(seen) else len(seen)