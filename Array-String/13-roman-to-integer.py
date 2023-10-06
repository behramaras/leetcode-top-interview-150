class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = 0
    
        for i in s:
            result += numerals[i]
            
        if "IV" in s:
            result -= s.count("IV") * 2
        if "IX" in s:
            result -= s.count("IX") * 2
        if "XL" in s:
            result -= s.count("XL") * 20
        if "XC" in s:
            result -= s.count("XC") * 20
        if "CD" in s:
            result -= s.count("CD") * 200
        if "CM" in s:
            result -= s.count("CM") * 200

        return result
