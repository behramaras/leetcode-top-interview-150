class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = ""
        
        for i in s:
            if i.isalpha() or i.isnumeric():
                t += i.lower()
        if t == t[::-1]:
            return True
        return False
