class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str2 in str1:
            c = ""
            a = ""
            for i in range(len(str2)):
                a += str2[i]
                if a in str1:
                    if str1.replace(a,"") == "" and str2.replace(a,"") == "":
                        c = a
            return c
        elif str1 in str2:
            c = ""
            a = ""
            for i in range(len(str1)):
                a += str1[i]
                if a in str2:
                    if str2.replace(a,"") == "" and str1.replace(a,"") == "":
                        c = a
            return c
        else:
            return ""