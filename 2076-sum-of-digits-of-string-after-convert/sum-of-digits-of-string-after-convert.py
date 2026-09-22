class Solution(object):
    def getLucky(self, str, k):
        char = "0abcdefghijklmnopqrstuvwxyz"
        s = 0
        for el in str:
            i = char.index(el)
            if i < 10:
                s = s * 10 + i
            else:
                s = s * 100 + i 

        for i in range(k):
            su = 0
            while s != 0:
                su += s%10
                s //= 10
            s = su
        return s