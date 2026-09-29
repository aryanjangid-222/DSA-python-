class Solution(object):
    def checkIfPangram(self, sentence):
        check = list(set(sentence))
        return len(check) == 26