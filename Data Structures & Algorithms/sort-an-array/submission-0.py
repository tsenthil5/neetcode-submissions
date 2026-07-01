class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr)//2
            leftArr = mergeSort(arr[:mid])
            rightArr = mergeSort(arr[mid:])
            return merge(leftArr, rightArr)

        def merge(leftArr, rightArr):
            left, right = 0, 0
            sortedArr = []
            idx = 0
            while left < len(leftArr) and right < len(rightArr):
                if leftArr[left] <= rightArr[right]:
                    sortedArr.append(leftArr[left])
                    left+=1

                else:
                    sortedArr.append(rightArr[right])
                    right+=1

            
            sortedArr.extend(leftArr[left:])
            sortedArr.extend(rightArr[right:])

            return sortedArr   

        return mergeSort(nums)






        