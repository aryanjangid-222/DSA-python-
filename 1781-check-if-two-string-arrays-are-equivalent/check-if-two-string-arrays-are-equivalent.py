class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        a = ""
        b = ""
        for el in word1:
            a += el
        for el in word2:
            b += el
        return a==b
        