class Solution1(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([i for i in sorted(nums)[::2]])
# just beat 90%, there's still faster method

# we can change sum([i for i in sorted(nums)[::2]]) to 
# sum(sorted(nums)[::2])


class Solution2(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
