class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # traversal a lsit and remember the head at one time, once we get a new element a, list[head] = a and head += 1
        # once we get a same element tail += 1
        # after the traversal, we remove the tail of the list with the length of tail
        # then we return _len - tail
        if nums is None or len(nums)==0:
            return 0
        _len = len(nums)
        head = 0
        tail = 0
        for i in xrange(1,_len):
            now = nums[i]
            if now == nums[head]:
                tail += 1
            else:
                nums[head+1] = now
                head += 1
        for i in range(tail):
            nums.pop()
        return _len - tail
        
