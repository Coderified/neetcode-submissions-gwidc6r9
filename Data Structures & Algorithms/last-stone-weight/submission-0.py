class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [-x for x in stones]
        heapq.heapify(nums)
        while len(nums)>=1:
            
            if len(nums)==1:
                return -nums[0]
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)
            heapq.heappush(nums,a-b)
            print(nums)

        
