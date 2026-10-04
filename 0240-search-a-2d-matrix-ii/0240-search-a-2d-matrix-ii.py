class Solution(object):
    def searchMatrix(self, mat, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows=len(mat)
        cols=len(mat[0])
        row=0
        col=cols-1
        while row<rows and col>=0:
            if mat[row][col]==target:
                return True
            elif mat[row][col]<target:
                row+=1
            else:
                col-=1
        return False                
        