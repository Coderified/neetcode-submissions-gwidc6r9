class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for x in coins:
                if i-x>=0:
                    dp[i]=min(dp[i],1+dp[i-x])

        if dp[amount]!=amount+1:
            return dp[amount]
        else:
            return -1

        