class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        ware = {}
        for i in range(len(nums)):
            head = nums[i]
            if head in ware:
                if i-ware[head] <= k:
                    return True
            ware[head] = i
        return False
