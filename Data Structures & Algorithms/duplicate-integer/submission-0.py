class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        for item in nums:
            if item in numsSet:
                return True
            numsSet.add(item)
        return False

         