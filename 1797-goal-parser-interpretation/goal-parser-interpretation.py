class Solution(object):
    def interpret(self, command):
        a = 0
        c = -1
        res = ""
        for i in command:
            c += 1
            if a!=0:
                a -= 1
                continue
            if i=="G":
                res += "G"
            elif i=="(" and command[c+1]==")":
                res += "o"
                a = 1
            elif i=="(" and command[c+1]=="a":
                res += "al"
                a = 3
        return res