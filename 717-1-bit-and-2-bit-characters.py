class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        _len = len(bits)
        i = 0
        start = 0
        while i < _len:
            if bits[i] == 0:
                start = i
                i += 1
            elif bits[i] == 1:
                start = i
                i += 2
        if _len-start == 2:
            return False
        else:
            return True
