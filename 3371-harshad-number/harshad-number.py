class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        num = x
        s = 0
        while num != 0:
            s += num%10
            num = num//10
        if x % s == 0:
            return s
        return -1
        