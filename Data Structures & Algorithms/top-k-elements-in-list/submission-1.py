class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts={}
        l=[]
        for i in range(len(nums)+1):
            l.append(list())


        for items in nums:
            counts[items] = counts.get(items,0)+1
        for n,c in counts.items():
            l[c].append(n)
        
        ll=[]
        for j in range(len(l)-1,-1,-1):
            for nums in l[j]:
                ll.append(nums)

                if len(ll)==k:
                    return ll
        
        