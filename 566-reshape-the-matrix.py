class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        or_num = len(nums)*len(nums[0])
        if or_num != r*c:
            return nums
        mid = []
        for i in nums:
            mid += i
        re = []
        for j in range(r):
            re.append(mid[j*c:(j+1)*c])
        return re
        
