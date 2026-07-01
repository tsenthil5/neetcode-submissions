class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res+=str(len(string)) + "#" + string


        return res 

    def decode(self, s: str) -> List[str]:
        print(s)
        res_list = []
        pointer = 0
        while pointer != len(s):
            stringLen = ""
            while s[pointer] != "#":
                stringLen+=s[pointer]
                pointer+=1
            currLen = int(stringLen)
            res_list.append(s[pointer+1:pointer+currLen+1])
            pointer = pointer+currLen+1

        return res_list





    '''
    are special characters allowed in UTF-8? #,? etc
    string manipulation

    iterate through the list
    check if character is #
    if not # then concatenate string with

    string = ["senthil", "thanneermalai", "cat", "#dog"]

    6#senthil11#thanneermalai3#cat 
    '''


