class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        nums = [1,2,3,4]
        target = 3
        res = [[1,1,1],[1,1,2],[3]]

        1) sort the array
        2) at each index, consider the element
        3) if sum > target, then backtrack
        4) when backtrack, we will skip the current element
        5) repeat 2)
        '''
        def backtrack(currSum, currArray, index):
            if currSum == target:
                res.append(currArray.copy())
                return

            if currSum > target:
                return 

            if index == len(nums):
                return

            currArray.append(nums[index])
            currSum+=nums[index]
            backtrack(currSum, currArray, index)
            currArray.pop()
            currSum-=nums[index]
            backtrack(currSum, currArray, index+1)


        res = []
        backtrack(0, [], 0)
        return res

        '''
        nums = [1,2,3,4]
        target = 3
        backtrack(0, [], 0)
        ca = [1]
        cs = 1
        ca = [1,1,1]
        cs = 3

        '''


        