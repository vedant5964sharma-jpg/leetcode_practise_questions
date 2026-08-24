class Solution(object):
    def countNegatives(self, grid):
        count=0
        for row in grid:
            for element in row:
                if element<0:
                    count+=1
        return count            