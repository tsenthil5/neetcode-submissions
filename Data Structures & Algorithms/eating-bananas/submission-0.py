class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        def pilesConsume(mid):
            total = 0
            for p in piles:
                total+=math.ceil(p/mid)

            return total

        def binary_search(piles, h):
            left, right = 1, max(piles)
            minHr = max(piles)
            while left <= right:
                mid = (left+right)//2
                if pilesConsume(mid) <= h:
                    minHr = mid
                    right = mid - 1

                elif pilesConsume(mid) > h:
                    
                    left = mid+1
            return minHr
            


        return binary_search(piles, h)




        