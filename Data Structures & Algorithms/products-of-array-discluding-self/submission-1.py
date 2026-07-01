class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix = [1, 2, 8, 48]
        suffix = [48,48,24,6]
        '''
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        for idx in range(0, len(nums)):
            if idx == 0:
                prefix[idx] = nums[idx]
            else:
                prefix[idx] = nums[idx] * prefix[idx-1]

        for idx in range(len(nums)-1, -1, -1):
            if idx == len(nums)-1:
                suffix[idx] = nums[idx]

            else:
                suffix[idx] = nums[idx]*suffix[idx+1]


        res = [1]*len(nums)
        for idx in range(len(nums)):
            if idx == 0:
                res[idx] = suffix[idx+1]

            elif idx == len(nums)-1:
                res[idx] = prefix[idx-1]

            else:
                res[idx] = prefix[idx-1] * suffix[idx+1]


        return res

        