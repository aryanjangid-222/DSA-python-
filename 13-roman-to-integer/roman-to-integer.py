class Solution(object):
    def romanToInt(self, s):
        a = 0
        b = 1
        e = 0
        ans = 0
        l = len(s)
        val = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1
            }
        if len(s)==1:
            return val[s]
        for i in range(l-1):
            if i==l-2:
                b = 2
            if a!=0:
                a = 0
                if b==2:
                    e = 1
                else:
                    continue
            if val[s[i]]<val[s[i+1]]:
                a =  val[s[i+1]]-val[s[i]]
                ans += a
            else:
                if e==1:
                    b = 1
                for j in range(b):
                    ans +=  val[s[i+j+e]]
        return ans

            