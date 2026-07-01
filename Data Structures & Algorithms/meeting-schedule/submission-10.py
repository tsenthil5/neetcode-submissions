"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda x: x.start)
        #for i in intervals:
            #print([i.start, i.end])
        for idx, ele in enumerate(intervals):
            if idx == 0:
                prevStart = ele.start
                prevEnd = ele.end


            else:
                if ele.start < prevEnd:
                    return False

            prevStart = ele.start
            prevEnd = ele.end

        return True

