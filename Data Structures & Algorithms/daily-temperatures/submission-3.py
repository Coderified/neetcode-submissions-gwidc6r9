class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        l=[0]*n
        stack = []

        for idx,val in enumerate(temperatures):
            # print(idx,val)
           
            if len(stack)==0 or stack[-1][1]>val:
                stack.append((idx,val))
            else:
                while len(stack)>0 and val>stack[-1][1]:
                    a=stack.pop()
                    l[a[0]] = idx-a[0]
                stack.append((idx,val))
            # print(stack) 
            


        return l

            
        