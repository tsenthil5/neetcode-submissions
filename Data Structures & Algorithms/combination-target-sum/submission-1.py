class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def combiSum(ptr, currArr, currSum):
            if ptr >= len(nums):
                return 
            if currSum > target:
                return
            if currSum == target:
                res.append(currArr.copy())
                return
            currArr.append(nums[ptr])
            combiSum(ptr, currArr, currSum+nums[ptr])
            currArr.pop()
            combiSum(ptr+1, currArr, currSum)


        combiSum(0, [], 0)
        return res


        

        