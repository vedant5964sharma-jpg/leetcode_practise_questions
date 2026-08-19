class Solution(object):
    def setZeroes(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        row_track=[0 for i in range(rows)]
        cols_track=[0 for i in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row_track[i]=-1
                    cols_track[j]=-1
        for i in range(rows):
            for j in range(cols):
                if row_track[i]==-1 or cols_track[j]==-1:
                    matrix[i][j]=0            