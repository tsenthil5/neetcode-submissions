class Solution:

    def encode(self, strs: List[str]) -> str:
        oneString = ""
        for i in strs:
            
            oneString+=str(len(i))
            oneString+="#"
            oneString+=i

        return oneString


    def decode(self, s: str) -> List[str]:
        charIdx = 0
        res = []
        while(charIdx != len(s)):
            tempLength = ""
            while(s[charIdx]!="#"):
                tempLength+=s[charIdx]
                charIdx+=1

            temp = ""
            charIdx+=1
            tempLength = int(tempLength)
            while(tempLength!=0):
                temp+=s[charIdx]
                charIdx+=1
                tempLength-=1

            res.append(temp)
        return res
            
