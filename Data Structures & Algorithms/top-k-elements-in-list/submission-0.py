class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for items in nums:
            d[items]=d.get(items,0)+1
        
        descsort = dict(sorted(d.items(),key=lambda item:item[1],reverse=True))

        print(descsort)
        
        return list(descsort.keys())[:k]
        