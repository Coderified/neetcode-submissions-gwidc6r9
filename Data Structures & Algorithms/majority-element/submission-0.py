class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=defaultdict(int)

        for items in nums:
            d[items]+=1
        return max(d,key=d.get)
        