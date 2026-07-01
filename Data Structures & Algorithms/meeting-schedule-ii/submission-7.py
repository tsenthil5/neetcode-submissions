"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq as hq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minHeap = []
        intervals.sort(key=lambda intervals:intervals.start)
        room = float('-inf')
        for interval in intervals:
            if not minHeap:
                hq.heappush(minHeap, interval.end)

            else:
                if minHeap[0] <= interval.start:
                    hq.heappop(minHeap)
                    hq.heappush(minHeap, interval.end)

                else:
                    hq.heappush(minHeap, interval.end)
            room = max(room, len(minHeap))

        if room == float('-inf'):
            return 0
        else:
            return room
        

        