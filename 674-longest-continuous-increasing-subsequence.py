class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        re = 1
        cursor = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cursor += 1
            else:
                cursor = 1
            re = max(re, cursor)
        return re
