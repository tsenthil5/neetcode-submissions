import heapq as hq
class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        max heap 
        store it in tempDict if count not 0
        discard if count 0

        if heap empty and temp count>1 return false
        '''

        maxHeap = []
        countDict = {}
        res = ""
        tempList = []
        for char in s:
            countDict[char] = countDict.get(char, 0)+1

        for key, val in countDict.items():
            hq.heappush(maxHeap, [-1*val, key])

        while maxHeap:
            countChar, char = hq.heappop(maxHeap)
            countChar = -1*countChar
            res+=char
            countChar-=1
            if tempList:
                hq.heappush(maxHeap, [-1*tempList[0], tempList[1]])
                tempList = []

            if countChar > 0:
                tempList = [countChar, char]

        return res if not tempList else ""






        