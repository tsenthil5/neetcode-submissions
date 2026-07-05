class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subSetSum = sum(nums)/k
        visited = [False]*len(nums)
        def backtracking(idx, currSum, k):

            if k == 0:
                return True
            if currSum == subSetSum:
                return backtracking(0, 0, k-1)


            for i in range(idx, len(nums)):
                if not visited[i]:
                    
                    if currSum + nums[i] > subSetSum:
                        continue
                    visited[i] = True
                    if backtracking(i+1, currSum+nums[i], k):
                        return True

                    visited[i] = False

            return False

        return backtracking(0, 0, k)






        

            


        