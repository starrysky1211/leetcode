class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = set(nums)
        re = []
        for i in xrange(1, n+1):
            if i not in nums:
                re.append(i)
        return re
