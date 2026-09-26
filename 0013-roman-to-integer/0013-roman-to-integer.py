class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = {

            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n=len(s)
        i=0
        result=0
        for i in range (n):
            if i<n-1 and letter[s[i]]<letter[s[i+1]]:
                result-=letter[s[i]]
            else:
                result+=letter[s[i]]
        return result            