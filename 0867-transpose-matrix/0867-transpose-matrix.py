class Solution(object):
    def transpose(self, matrix):
       n=len(matrix)
       m=len(matrix[0])
       ans=[[0]*n for _ in range(m)]
       for i in range(n):
        for j in range(m):
            ans[j][i]=matrix[i][j]
       return ans      
        