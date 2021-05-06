class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s_nums = sorted(nums)
        _len = len(nums)
        head = 0
        tail = _len
        for i in range(len(nums)):
            if s_nums[i] != nums[i]:
                break
            else:
                head += 1
        for i in range(len(nums)):
            if s_nums[_len-i-1] != nums[_len-i-1]:
                break
            else:
                tail -= 1
        return max(tail-head, 0)
