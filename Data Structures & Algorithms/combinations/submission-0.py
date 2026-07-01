class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        [1,2,3]
        [1,2], [1,3], [2,3]

        base cases:
        if length(currarr) > k
        if currPtr >= n
        '''

        res = []
        def formArray(currPtr, currArr):
            if len(currArr) == k:
                res.append(currArr.copy())
                return
            if currPtr >n:
                return

            if len(currArr) > k:
                return



            currArr.append(currPtr)
            formArray(currPtr+1, currArr)
            currArr.pop()
            formArray(currPtr+1, currArr)

        formArray(1, [])
        return res

             

        