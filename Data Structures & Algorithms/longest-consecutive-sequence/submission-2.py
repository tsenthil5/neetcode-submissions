class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxNum = 0
        nums = set(nums)
        for idx, n in enumerate(nums):
            startSeq = 0
            currNum = n
            if currNum-1 not in nums:
                while currNum in nums:
                    startSeq+=1
                    currNum+=1

            maxNum = max(maxNum, startSeq)
        return maxNum


                
                  
        