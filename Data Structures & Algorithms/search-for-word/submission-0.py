class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

            s=''
            rows = len(board)
            cols = len(board[0])
            i=0
            path=set()
            def dfs(r,c,word,i,s):
                
                if s==word:
                    return True   
                if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[i] or (r,c) in path:
                    return False
                    
                s+=word[i]
                print(s)
                path.add((r,c)) 

                i+=1
                
                found =  (dfs(r+1,c,word,i,s) or
                dfs(r-1,c,word,i,s) or
                dfs(r,c+1,word,i,s) or
                dfs(r,c-1,word,i,s))

                path.remove((r,c))

                return found
            

            for r in range(rows):
                    for c in range(cols):
                        if dfs(r,c,word,i,s):
                            return True
            return False