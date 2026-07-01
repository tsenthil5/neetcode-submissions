class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        k = 1
        while left <= right:
            if s[left] != s[right]:
                newStr = s[:left] + s[left+1:]
                #print(newStr)
                if newStr!=newStr[::-1]:
                    k-=1
                
                newStr = s[:right] + s[right+1:]
                #print(newStr)
                if newStr!= newStr[::-1] and k == 0:
                    return False
                
                return True


            else:
                left+=1
                right-=1

        return True



        