class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 先找到众数，再看最先和最后的index
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i]+= 1
            else:
                hashmap[i] = 1
        maxi = -1
        minz = len(nums)
        lis = []
        for key in hashmap:
            if hashmap[key] > maxi:
                maxi = hashmap[key]
        if maxi == 1:
            return 1
        for key in hashmap:
            if hashmap[key] == maxi:
                lis.append(key)
        for i in lis:
            left = 0
            right = len(nums) - 1
            while nums[left] != i:
                left += 1
            while nums[right] != i:
                right -= 1
            if minz > (right - left + 1):
                minz = right - left+1
        return minz
