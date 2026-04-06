class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(1+len(s))

        dp[len(s)] = True
        end = len(s)

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                # print(w,i)
                if w == s[i:i+len(w)]:
                    if dp[i+len(w)] is True:
                        dp[i]=dp[i+len(w)]
                        break
                    
                    
            print(dp)
        return dp[0]

        

        


        

        


        