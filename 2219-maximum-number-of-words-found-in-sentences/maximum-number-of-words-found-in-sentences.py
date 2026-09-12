class Solution(object):
    def mostWordsFound(self, sentences):
        max_word = 0
        for el in sentences:
            c = el.count(" ")
            if c > max_word:
                max_word = c
        
        return max_word + 1