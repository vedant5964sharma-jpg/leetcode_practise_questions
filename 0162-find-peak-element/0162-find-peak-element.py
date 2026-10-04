class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        left=0
        high=n-1
        while left<high:
            mid=(left+high)//2
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                high=mid
        return left            