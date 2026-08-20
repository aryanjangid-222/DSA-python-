class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        res = arrivalTime + delayedTime
        if res>23:
            res -= 24
        return res