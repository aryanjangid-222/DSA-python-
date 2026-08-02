class Solution(object):
    def checkIfPangram(self, sentence):
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for el in alpha:
            if sentence.count(el)>0:
                continue
            else:
                return False
        return True 