class Solution(object):
    def findComplement(self, num):
        a = format(num,'b')
        b = ""
        for i in a:
            if i=="1":
                b += "0"
            else:
                b += "1"
        return int(b,2)
        
        