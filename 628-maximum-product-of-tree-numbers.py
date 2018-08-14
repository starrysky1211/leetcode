# a simple solution:
class Solution1(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s_n = sorted(nums)
        nl = s_n[:2]
        pl = s_n[-3:]
        return max(nl[0]*nl[1]*pl[-1], pl[0]*pl[1]*pl[2])

# a faster solution:
class Solution2(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        min1, min2 = float('inf'), float('inf')
        
        for i in nums:
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i
        return max(max3*max2*max1, max1*min1*min2)
