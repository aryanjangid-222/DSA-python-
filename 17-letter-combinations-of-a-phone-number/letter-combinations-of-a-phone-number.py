class Solution(object):
    def letterCombinations(self, s):
        check = [0,0,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        l = len(s)
        res = []
        if l==1:
            for el in check[int(s)]:
                res.append(el)
            return res
        elif l==2:
            for el_1 in check[int(s[0])]:
                for el_2 in check[int(s[1])]:
                    res.append(el_1+el_2)
            return res
        elif l==3:
            for el_1 in check[int(s[0])]:
                for el_2 in check[int(s[1])]:
                    for el_3 in check[int(s[2])]:
                        res.append(el_1+el_2+el_3)
            return res
        elif l == 4:
            for el_1 in check[int(s[0])]:
                for el_2 in check[int(s[1])]:
                    for el_3 in check[int(s[2])]:
                        for el_4 in check[int(s[3])]:
                            res.append(el_1+el_2+el_3+el_4)
            return res