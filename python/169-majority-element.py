class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in set(nums):
            c = nums.count(i)
            if c > n // 2:
                return i
"""
there's a better solution: we can sort the array and get the middle element, it must be the majorityElement
"""


class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        return nums[n//2]

