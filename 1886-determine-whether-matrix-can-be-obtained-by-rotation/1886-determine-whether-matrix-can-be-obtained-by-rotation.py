class Solution(object):
    def findRotation(self, mat, target):
       n=len(mat)
       for i in range(4):
        if mat==target:

            return True
        for i in range(0,n-1):
            for j in range(i+1,n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        for row in mat:
            row.reverse()
       return False    

