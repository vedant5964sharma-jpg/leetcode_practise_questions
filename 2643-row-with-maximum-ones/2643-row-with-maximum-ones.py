class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max_ones=0
        answer_row=0
        for i in range(len(mat)):
            count=0
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    count+=1
            if count>max_ones:
                max_ones=count
                answer_row=i
        return [answer_row,max_ones]        

