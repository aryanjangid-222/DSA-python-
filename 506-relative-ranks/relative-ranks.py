class Solution(object):
    def findRelativeRanks(self, score):
        out = []
        check = [el for el in score]
        check.sort()
        check = check[::-1]
        for el in score:
            c = check.index(el)
            if c<3:
                if c==0:
                    out.append("Gold Medal")
                elif c==1:
                    out.append("Silver Medal")
                else:
                    out.append("Bronze Medal")
            else:
                out.append(str(c+1))
        return out

