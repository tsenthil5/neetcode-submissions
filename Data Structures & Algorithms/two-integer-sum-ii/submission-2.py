class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start <end:
            currStart = start
            for ptr in range(currStart, end+1, 1):
                if numbers[ptr] + numbers[currStart] == target:
                    return [currStart+1, ptr+1]

                elif numbers[ptr] + numbers[currStart] > target:
                    end = ptr
                    break

            start+=1
                    



        


        