import heapq as hq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key= lambda x:x[1])
        minHeap = []
        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                capacity+=hq.heappop(minHeap)[1]

            
            capacity-=numPass
            if capacity < 0:
                return False
            hq.heappush(minHeap, [end, numPass])

        return True
            

        