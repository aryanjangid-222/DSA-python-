class Solution(object):
    def largestOddNumber(self, num):
        ch = num[::-1]
        a = 0
        for el in ch:
            a += 1
            if int(el)%2!=0:
                a -= 1
                break
        return num[0:len(num)-a] 