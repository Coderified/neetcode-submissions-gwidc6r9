class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #rows = len txt1 + 1
        #cols = len txt2 + 1

        grid = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    grid[i+1][j+1]=grid[i][j]+1
                else:
                    grid[i+1][j+1]=max(grid[i][j+1],grid[i+1][j])

        return grid[len(text1)][len(text2)]