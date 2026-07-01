class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            currCount = [0]*26
            for char in string:
                currCount[ord(char)-ord('a')]+=1

            result[tuple(currCount)].append(string)

        return result.values()
        