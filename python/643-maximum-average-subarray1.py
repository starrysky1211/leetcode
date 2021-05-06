class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # dp solution 每多加一个元素，就要比较原来的最大值和新数组的后k个数的平均值
        _len = len(nums)
        if k > _len:
            return 0
        av = sum(nums[:k])
        last = av
        for i in range(k, _len):
            last += nums[i] - nums[i-k]
            av = max(av, last)
        return av/float(k)
        
