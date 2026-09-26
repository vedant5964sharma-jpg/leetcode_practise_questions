class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        for ch in s:
            if len(ans)<2 or not (ans[-1]==ch and ans[-2]==ch):
                ans+=ch
        return ans        