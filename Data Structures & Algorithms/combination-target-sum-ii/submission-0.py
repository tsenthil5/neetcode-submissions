class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def combiSum(ptr, currArr, currSum):
            if currSum == target:
                res.append(currArr.copy())
                return
            if ptr >= len(candidates):
                return 
            if currSum > target:
                return

            currArr.append(candidates[ptr])
            combiSum(ptr+1, currArr, currSum+candidates[ptr])
            currArr.pop()
            while ptr+1 < len(candidates) and candidates[ptr] == candidates[ptr+1]:
                ptr+=1
            combiSum(ptr+1, currArr, currSum)


        combiSum(0, [], 0)
        return res
        