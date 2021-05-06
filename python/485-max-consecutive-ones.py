class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = []
        time = 0
        for i in nums:
            if not i:
                times.append(time)
                time = 0
            else:
                time += 1
        times.append(time)
        return max(times)
