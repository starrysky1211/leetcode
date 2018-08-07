class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # use bi-search
        if not nums:
            return 0
        
        _len = len(nums)
        head = 0
        tail = _len - 1
        while head < tail:
            mid = (tail + head) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                tail = mid
            else:
                head = mid + 1
        if target <= nums[head]:
            return head
        else:
            return head + 1
        
