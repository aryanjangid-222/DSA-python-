class Solution(object):
    def findWords(self, words):
        res = []
        a = 'qwertyuiopQWERTYUIOP'
        b = 'asdfghjklASDFGHJKL'
        c = 'zxcvbnmZXCVBNM'
        for el in words:
            if el[0] in a:
                li = list(set(el))
                for i in li:
                    if i in a:
                        continue
                    el = ""
                    break
            elif el[0] in b:
                li = list(set(el))
                for i in li:
                    if i in b:
                        continue
                    el = ""
                    break
            else:
                li = list(set(el))
                for i in li:
                    if i in c:
                        continue
                    el = ""
                    break
            if el != "":
                res.append(el)
        return res