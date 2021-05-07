#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return 0
        dic = {}
        for i in range(len(nums)):
            cur = nums[i]
            if cur in dic:
                return [dic[cur], i]
            else:
                dic[target-cur] = i
# @lc code=end

