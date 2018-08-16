class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _sum = sum(nums)
        pre = 0
        for i in range(len(nums)):
            if pre*2 == _sum-nums[i]:
                return i
            pre += nums[i]
        return -1
