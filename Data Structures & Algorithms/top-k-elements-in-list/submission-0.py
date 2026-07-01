import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}
        maxHeap = []
        result = []
        for number in nums:
            freqCount[number] = freqCount.get(number, 0)+1

        for key, value in freqCount.items():
            maxHeap.append((-1*value, key))

        heapq.heapify(maxHeap)
        while k>0:
            result.append(heapq.heappop(maxHeap)[1])
            k-=1

        return result



        
        