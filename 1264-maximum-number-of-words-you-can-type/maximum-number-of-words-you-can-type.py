class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        word = text.split()
        n = 0
        for el in word:
            for char in el:
                if char in brokenLetters:
                    n -= 1
                    break
            n += 1
            
        return n