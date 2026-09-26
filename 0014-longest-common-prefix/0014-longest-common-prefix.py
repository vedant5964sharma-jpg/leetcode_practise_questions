class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=strs[0]
        for s in strs:
            i=0
            while i<len(prefix) and i<len(s) and prefix[i]==s[i]:
                i+=1
            prefix=prefix[:i]  
        return prefix      
        