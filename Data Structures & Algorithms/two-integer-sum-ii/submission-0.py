class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        preSum = {}
        for idx, n in enumerate(numbers):
            if n in preSum:
                return [preSum[n]+1, idx+1]
            preSum[target-n] = idx

        


        