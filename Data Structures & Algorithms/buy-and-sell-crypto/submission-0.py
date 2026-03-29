class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mins = prices[0]
        maxs=0
        i=1
        while i <len(prices):
            if prices[i]<mins:
                mins=prices[i]
                i+=1
            else:
                maxs = max(maxs,prices[i]-mins)
                i+=1

        return maxs



        