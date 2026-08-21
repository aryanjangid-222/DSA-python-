class Solution(object):
    def countWords(self, words1, words2):
        a = 0
        if len(words1)>len(words2):
            for el in words2:
                if el in words1:
                    if words1.count(el) == 1 and words2.count(el)==1:
                        a += 1
            return a
        for el in words1:
            if el in words2:
                if words1.count(el) == 1 and words2.count(el)==1:
                    a += 1
        return a