class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {}
        for index, value in enumerate(nums):
            if value in visit:
                return [visit[value], index]

            else:
                visit[target-value] = index 

        