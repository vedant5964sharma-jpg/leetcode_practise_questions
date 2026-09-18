class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count={}
        n=len(nums)
        ans=[]
        
        for x in  nums:
            if x in count:
                count[x]+=1
            else:
                count[x]=1    
        for x in count:
            if count[x]>n//3:
                ans.append(x)
        return ans                