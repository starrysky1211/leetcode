class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = None
        for i in sorted(nums):
            if i == last:
                return True
            else:
                last = i
        return False
        
