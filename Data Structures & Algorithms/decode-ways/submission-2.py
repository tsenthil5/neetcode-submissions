class Solution:
    def numDecodings(self, s: str) -> int:


        def dfs(idx):
            if idx >= len(s):
                return 1

            if s[idx] == "0":
                return 0

            if idx in cache:
                return cache[idx]

            totalWays = 0
            currString = ""
            currString+=s[idx]
            totalWays+=dfs(idx+1)
            if idx+1 < len(s):
                currString += s[idx+1]
                if int(currString) <= 26: 
                    totalWays+=dfs(idx+2)

            cache[idx] = totalWays
            return totalWays

        cache = {}
        return dfs(0)
        
                

        