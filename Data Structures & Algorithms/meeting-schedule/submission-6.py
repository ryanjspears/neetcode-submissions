"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #bubble sort
        ints = intervals
        j = len(ints) - 1
        while j > 0:
            p = 0
            while p < j:
                cur = ints[p].start
                nex = ints[p+1].start
                if cur > nex:
                    tmp = ints[p]
                    ints[p] = ints[p+1] 
                    ints[p+1] = tmp

                p+=1
            j-=1

        #print sorted
        for i in ints:
            print(f"s={i.start} e={i.end}")

        #sorted on start time
        i = 0
        while i < len(ints) - 1:
            print(f"1={ints[i].end} 2={ints[i+1].start}")
            if ints[i].end > ints[i+1].start:
                return False
            i += 1

        return True