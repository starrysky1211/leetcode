class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        large1 = (float('-inf'), -1)
        large2 = (float('-inf'), -1)
        if len(nums) < 2:
            return 0
        for i in range(len(nums)):
            if nums[i] > large1[0]:
                large2 = large1
                large1 = (nums[i], i)
            elif nums[i] > large2[0]:
                large2 = (nums[i], i)
        if large1[0] >= large2[0]*2:
            return large1[1]
        else:
            return -1
