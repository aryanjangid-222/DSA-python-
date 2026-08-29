class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        while num > 9:
            sum = 0
            for el in str(num):
                sum += int(el)
            if sum < 10:
                return sum
            else:
                num = sum