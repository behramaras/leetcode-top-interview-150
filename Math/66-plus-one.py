class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            i = len(digits) -1
            while i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits
                if i == 0 and digits[i] == 0:
                    new_digits = digits[:]
                    new_digits.insert(0,1)
                    return new_digits
                
                i -= 1

        return digits
        
