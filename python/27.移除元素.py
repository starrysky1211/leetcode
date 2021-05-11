#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
    def removeElement1(self, nums: List[int], val: int) -> int:
        # 首尾指针
        tile = len(nums)-1
        head = 0
        while head <= tile:
            if nums[head] == val:
                nums[head] = nums[tile]
                tile -= 1
            else:
                head += 1
        return head
# @lc code=end

