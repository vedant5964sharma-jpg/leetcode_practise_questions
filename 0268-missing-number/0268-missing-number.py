class Solution(object):
    def missingNumber(self, nums):
        sum=0
        actual=0
        n=len(nums)
        for i in range(0,n):
            sum+=nums[i]
        actual=((n+1)*n)/2
        return actual-sum    
       