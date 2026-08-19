class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for el in ransomNote:
            if ransomNote.count(el)>magazine.count(el):
                return False
        else:
            return True