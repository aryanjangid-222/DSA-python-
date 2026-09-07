class Solution(object):
    def firstPalindrome(self, words):
        for el in words:
            if el[::-1] == el:
                return el
        return ""