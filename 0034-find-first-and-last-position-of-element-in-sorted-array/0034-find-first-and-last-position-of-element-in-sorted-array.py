class Solution(object):
    def lower(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        lb=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    def upper(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        ub=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub     

    def searchRange(self, nums, target):
        lb=self.lower(nums,target)
        if lb == -1 or nums[lb] != target:
            return [-1, -1]
        
        ub=self.upper(nums,target)
        return[lb,ub-1]
       