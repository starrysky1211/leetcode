class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 冒泡，每当碰到新的0，泡泡的尺寸就+1
        # 设定一个head和遍历的i，head=0，每遇到一个非零数，若head==i，head+=1,continue，否则nums[head]=val, nums[i]=0,head+=1.
        # 每遇到一个零，直接continue
        head = 0
        for i in range(len(nums)):
            if nums[i]:
                if head == i:
                    head += 1
                else:
                    nums[head] = nums[i]
                    nums[i] = 0
                    head += 1
