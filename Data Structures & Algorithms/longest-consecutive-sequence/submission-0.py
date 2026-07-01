class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLen = 0
        for num in nums:
            
            if num-1 in nums:
                continue

            else:
                currnum = num
                currLen = 0
                while currnum in numsSet:
                    currLen+=1
                    currnum+=1

                maxLen = max(currLen,maxLen)

        return maxLen

        