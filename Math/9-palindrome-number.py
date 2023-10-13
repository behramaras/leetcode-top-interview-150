class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        palid_list = [i for i in x][::-1]
        is_palid = "".join(palid_list)

        return x == is_palid
