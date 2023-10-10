class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        new = [i for i in magazine]
        for i in ransomNote:
            if i not in new:
                return False
            else:
                new.remove(i)
        return True
