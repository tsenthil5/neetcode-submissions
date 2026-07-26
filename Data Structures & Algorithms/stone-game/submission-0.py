class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        left, right = 0, len(piles)-1
        alice = 0
        totalSum = sum(piles)
        while left < right:
            alice+=max(piles[left], piles[right])
            left+=1
            right-=1


        if alice > totalSum-alice:
            return True

        return False

        