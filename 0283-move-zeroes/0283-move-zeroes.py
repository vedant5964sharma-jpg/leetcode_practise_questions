class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        for k in range (len(nums)):
            if nums[k]!=0:
                nums[k],nums[i]=nums[i],nums[k]
                i+=1

        
