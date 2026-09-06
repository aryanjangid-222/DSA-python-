class Solution(object):
    def stringMatching(self, words):
        out = []
        words.sort(key=len)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    out.append(words[i])
                    break
        
        return out