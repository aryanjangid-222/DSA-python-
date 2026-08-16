class Solution(object):
    def longestCommonPrefix(self, strs):
        if "" in strs:
            return ""
        a = 0
        out = ""
        past = ""
        for el in strs:
            if a == 0:
                past = el
                a = 1
                continue
            s = -1
            if len(past)<=len(el):
                for i in past:
                    s += 1
                    if i != el[s]:
                        break
                    else:
                        out += i
            else:
                for i in el:
                    s += 1
                    if i != past[s]:
                        break
                    else:
                        out += i
            past = out
            if out == "":
                return ""
            else:
                out = ""
        return past