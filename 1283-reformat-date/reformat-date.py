class Solution(object):
    def reformatDate(self, date):
        out = []
        a = 0
        if len(date)==12:
            a = 1
        months = [" " ,"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        d = date[0:2-a]
        m = months.index(date[5-a:8-a])
        y = date[9-a:]
        if int(d)<10:
            d = "0"+d
        if m<10:
            m = "0"+str(m)
        out.append(y)
        out.append("-")
        out.append(m)
        out.append("-")
        out.append(d)
        return "".join(map(str,out))

        