class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers)-1
        while left < right:
            while left > 0 and numbers[left] == numbers[left-1]:
                left+=1

            while right < len(numbers)-1 and numbers[right] == numbers[right+1]:
                right-=1
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]

            elif numbers[left] + numbers[right] > target:
                right-=1

            else:
                left+=1


        