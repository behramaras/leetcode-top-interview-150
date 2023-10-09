class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        new = ""
        for i in range(len(s)):
            if s[i] in t:
                new += s[i]
                t = t[t.index(s[i])+1:]
        if s == new:
            return True
        return False
        
