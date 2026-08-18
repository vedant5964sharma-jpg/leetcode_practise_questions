class Solution(object):
    def rearrangeArray(self, nums):

        n=len(nums)
        pos=0
        neg=1
        result=[0]*n
        for i in range(0,n):
            if nums[i]>=0:
                result[pos]=nums[i]
                pos+=2
            else:
                result[neg]=nums[i]
                neg+=2
        return result            
      
        