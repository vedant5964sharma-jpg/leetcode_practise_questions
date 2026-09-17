class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while(x!=0):
            rem=x%10
            x//=10
            ans=ans*10+rem
        ans=ans*sign
        if (ans>2**31-1 or ans<-(2**31)):
            return 0
            
            
        return ans    
        