class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        char = "abcdefghijklmnopqrstuvwxyz"
        for el in char:
            if ransomNote.count(el)>magazine.count(el):
                return False
        return True