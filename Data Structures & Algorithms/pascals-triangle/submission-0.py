class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows <2:
            return [[1]]
        dp=[[]]*numRows

        dp[0] = [1]
        dp[1] = [1,1]

        for i in range(2,numRows):
            l=[1]
            for x in range(1,len(dp[i-1])):
                l.append(dp[i-1][x]+dp[i-1][x-1])
            l.append(1)

            dp[i]=l
        return dp

        