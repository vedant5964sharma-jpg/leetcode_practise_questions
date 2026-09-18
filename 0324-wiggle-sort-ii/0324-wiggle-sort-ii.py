class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr=sorted(nums)
        n=len(nums)
        mid=(n+1)/2
        small=arr[:mid][::-1]
        big=arr[mid:][::-1]
        i=0
        for x in small:
            nums[i]=x
            i+=2
        i=1
        for x in big :
            nums[i]=x
            i+=2   