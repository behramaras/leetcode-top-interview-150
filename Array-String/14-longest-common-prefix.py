class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        size = len(strs)

        if size == 0:
            return ""
        if size == 1:
            return strs[0]
        else:
            strs.sort()
            end = min(len(strs[0]),len(strs[len(strs)-1]))
            i = 0
            s = ""
            while i<len(strs[0]):
                if strs[0][i] == strs[-1][i]:
                    s += strs[0][i]
                    i += 1
                else:
                    break
            return s


        
