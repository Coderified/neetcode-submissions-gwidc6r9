class Solution:
    '''Imagine we just found the first permutation [1, 2, 3]. 
Here is what happens in the computer's memory to get to [1, 3, 2]:

1. Backtrack: Remove 3 (Path: [1, 2, 3] → [1, 2])
The function bt(3, [1, 2, 3]) finishes because it hit the base case (depth == 3).

The computer "'returns'" to the previous function call: bt(2, [1, 2]).

It executes current_path.pop() (removing 3) and used_array[2] = False.

The loop for j at this level was at the last index, so this function call also finishes.

2. Backtrack: Remove 2 (Path: [1, 2] → [1])
The computer "'returns'" to the even earlier call: bt(1, [1]).

It executes current_path.pop() (removing 2) and used_array[1] = False.

Crucial: The loop at this level was at j = 1. The loop continues to the next j...

3. Pick 3 (Path: [1] → [1, 3])
The loop at Level 1 moves to j = 2 (which is the number 3).

used_array[2] is False, so it picks it: current_path.append(3).

It calls bt(2, [1, 3]).

4. Pick 2 (Path: [1, 3] → [1, 3, 2])
Inside bt(2, [1, 3]), the loop starts at j = 0.

Is 1 used? Yes. Is 3 used? Yes. Is 2 used? No!

It picks 2: current_path.append(2).

It calls bt(3, [1, 3, 2]), hits the base case, and Permutation #2 is saved.

Key Takeaway for Redoing it:
The for loop is what allows the code to try something else after it backtracks.

Down: The recursion bt() goes deeper into the tree.

Up: The pop() and False bring you back up a level.

Sideways: The for j in range moves you to the next possible choice on that same level.'''
    def permute(self, nums: List[int]) -> List[List[int]]:



        res=[]
        i=0
        used_array=len(nums)*[0] 

        def bt(i,l):
                    
            if i==len(nums):
                res.append(list(l))
                return
            
            for x in range(0,len(nums)):

                if used_array[x] == 0:

                    l.append(nums[x])
                    used_array[x]=1

                    bt(i+1,l)

                    l.pop()
                    used_array[x]=0
                    

           
        bt(0,[])
        return res
            
        
         