class Solution(object)::
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 不要只局限在对比，可以同时进行修改，如此可以获得更简单的对比情况
        can = True
        
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                if can:
                    if i == 1 or nums[i-2] <= nums[i]:
                        nums[i-1] = nums[i]
                    else:
                        nums[i] = nums[i-1]
                    can = False
                else:
                    return False
        return True
