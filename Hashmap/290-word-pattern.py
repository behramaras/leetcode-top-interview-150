class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        new_pattern = [i for i in pattern]
        new_s = s.split(" ")

        if len(new_pattern) != len(new_s):
            return False
        else:
            check_dict = {}

            for i in range(len(new_pattern)):
                if new_pattern[i] not in check_dict.keys():
                    check_dict[new_pattern[i]] = new_s[i] 
        
        res = {}
        for key, val in check_dict.items():
            res.setdefault(val, key)
        res = dict((v, k) for k, v in res.items())

        check_pattern = ""

        for i in pattern:
            if i in res:
                check_pattern += i
        
        check_s = ""
        
        for i in check_pattern:
            check_s += res[i]
        
        new_s = s.replace(" ","")

        if check_s == new_s:
            return True
        return False
