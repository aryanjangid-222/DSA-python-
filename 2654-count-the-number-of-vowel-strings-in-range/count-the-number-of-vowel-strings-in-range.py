class Solution(object):
    def vowelStrings(self, words, left, right):
        n = 0
        for i in range(left,right+1):
            word = words[i]
            if word[0] in "aeiou":
                if word[len(word)-1] in "aeiou":
                    n += 1
        return n 