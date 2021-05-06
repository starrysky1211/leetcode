class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ori = range(n+1)
        for i in nums:
            ori.remove(i)
        return ori[0]
# it's very slow and uses lots of space to store the nums, we can use sum to solve this


class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)//2-sum(nums)
