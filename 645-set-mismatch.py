class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0,0]
        a = sum(set(nums))
        res[0] = sum(nums)-a
        res[1] = sum(range(1,len(nums)+1))-a
        return res
