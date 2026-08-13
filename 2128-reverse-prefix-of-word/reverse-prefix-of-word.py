class Solution(object):
    def reversePrefix(self, word, ch):
        a = 0
        c = 0
        for i in word:
            a += 1
            if i == ch:
                c = 1
                break
        if c == 1:
            rev = word[0:a][::-1]
            word = word[a:]
            word = rev + word
        return word