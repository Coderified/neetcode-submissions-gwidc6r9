class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        post=[]
        p=1
        for n in nums:
            p*=n
            pre.append(p)
        p=1
        for n in nums[::-1]:
            p*=n
            post.append(p)
        post=post[::-1]
        
        print(pre,post)
        l=[1]*len(nums)
        l[0]=post[1]
        l[-1]=pre[-2]
        for i in range(1,len(nums)-1):
            l[i]=post[i+1]*pre[i-1]
        return l
            
        
        

        

        