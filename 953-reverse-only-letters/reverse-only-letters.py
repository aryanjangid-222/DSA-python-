class Solution(object):
    def reverseOnlyLetters(self, s):
        import string
        spa = string.punctuation
        num = "1234567890"
        out = ""
        rev = ""
        check = []
        check_1 = []
        a = -1
        for i in s:
            a += 1
            if spa.find(i)>=0 or num.find(i)>=0:
                check.append(a)
                check_1.append(i)
            else:
                rev += i
        rev = rev[::-1]
        a = -1
        c = 0
        s1 = 0
        for i in range(len(s)):
            if check.count(i)==1:
                out += check_1[s1]
                s1 += 1
                c += 1
            else:
                out += rev[i-c]
        return out