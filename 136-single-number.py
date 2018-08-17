class Solutioni1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        head = 0
        nums.sort()
        for i in range(len(nums)):
            if not flag:
                # the first num
                head = nums[i]
                flag = 1
            else:
                if nums[i] != head:
                    return nums[i-1]
                flag = 0
        return nums[-1]
# not using extra space but need more time, O(nlgn+n) -- O(nlgn) because of nums.sort()
# a faster way is to make a hashtable, and can be O(2n) -- O(n)
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashtable = {}
        for i in nums:
            hashtable[i] = hashtable.get(i,0) + 1
        for k, v in hashtable.items():
            if v == 1:
                return k
# another fastest way to do it in O(n) and using no extra space by "^"
class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
