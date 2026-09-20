class Solution(object):
    def countBits(self, n):
        out = []
        for i in range(n+1):
            n = i
            c = -1
            b = 0
            while n != 0:
                c += 1
                if n%2:
                    n -= 1
                    b = (1*(10**c)) + b
                else:
                    n /= 2
            n = 0
            while b != 0:
                if b % 10 == 1:
                    n += 1
                b //= 10
            out.append(n)
        return out