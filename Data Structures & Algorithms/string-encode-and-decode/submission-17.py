class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for words in strs:
            lenWord = len(words)
            newString+=str(lenWord)
            newString+="#"
            newString+=words
        return newString
            
    def decode(self, s: str) -> List[str]:
        index = 0
        res = []
        while index != len(s):
            
            lenWord = ""
            while s[index] != "#":
                lenWord+=s[index]
                index+=1
            lenWord = int(lenWord)
            index+=1
            currWord = ""
            endIndex = index+lenWord
            while index != endIndex:
                currWord+=s[index]
                index+=1
            res.append(currWord)

        return res
            


