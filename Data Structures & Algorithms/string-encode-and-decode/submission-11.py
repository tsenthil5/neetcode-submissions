class Solution:

    def encode(self, strs: List[str]) -> str:
        singleString = ""
        for s in strs:
            singleString+=str(len(s))
            singleString+="#"
            singleString+=s
        #print(singleString)
        return singleString

            

    def decode(self, s: str) -> List[str]:
        output = []
        charIdx = 0
        while(charIdx!=len(s)):
            nextLength = ""
            while(s[charIdx]!="#"):
                nextLength+=s[charIdx]
                charIdx+=1

            nextLength = int(nextLength)
            charIdx+=1
            #print(nextLength)
            output.append(s[charIdx:charIdx+nextLength])
            charIdx+=nextLength
            

                
        #print(output)
        return output
