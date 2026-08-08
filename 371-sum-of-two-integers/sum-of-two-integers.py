class Solution(object):
    def getSum(self, a, b):
        out = []
        if a<=0 and b<=0:
                for i in range((-1*a)):
                    out.append(1)
                for i in range((-1*b)):
                    out.append(1)
                return -(len(out))
        elif a<0:
            for i in range(-1*a,b):
                if i>0:
                    out.append(1)
            return len(out)
        elif b<0:
            if -1*b<a:
                for i in range(-1*b,a):
                    out.append(1)
                return len(out)
            for i in range(-1*b,a,-1):
                if i>0:
                    out.append(1)
            return -(len(out))
        else:
            for i in range(a):
                out.append(1)
            for i in range(b):
                out.append(1)
            return len(out)
        
        