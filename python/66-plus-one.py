class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        header = 1
        for i in range(len(digits)):
            header, digits[i] = divmod(digits[i] + header, 10)
        if header:
            digits.append(header)
        digits.reverse()
        return digits
