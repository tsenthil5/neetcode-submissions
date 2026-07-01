class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix =[]

        prefixSum = 1
        for num in nums:
            prefixSum*=num
            prefix.append(prefixSum)

        suffixSum = 1
        for numIdx in range(len(nums)-1,-1,-1):
            suffixSum*=nums[numIdx]
            suffix.insert(0, suffixSum)

        

        res = []
        for idx in range(len(nums)):
            if idx == 0:
                res.append(suffix[idx+1])

            elif idx == len(nums)-1:
                res.append(prefix[idx-1])

            else:
                res.append(suffix[idx+1]*prefix[idx-1])


        return res


        