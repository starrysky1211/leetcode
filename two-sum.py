class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # set a dict of target-nums[i]:i and traversal
        if nums is None or len(nums)==0:
            return 0
        dic = {}
        for i in xrange(len(nums)):
            base = nums[i]
            if base in dic:
                return [dic[base],i]
            else:
                dic[target-base]=i
        return 0
            
