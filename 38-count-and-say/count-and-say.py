class Solution(object):
    def countAndSay(self, n):
        res = "1"
        for i in range(n-1):
            pre = ""
            check = []
            for el in res:
                if el == pre:
                    check[len(check)-1] += el
                else:
                    pre = el
                    check.append(el)

            res = ""
            for el in check:
                res += str(len(el)) + el[0]
        
        return res        