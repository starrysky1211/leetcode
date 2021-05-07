#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (35.40%)
# Likes:    2780
# Dislikes: 0
# Total Accepted:    693K
# Total Submissions: 2M
# Testcase Example:  '123'
#
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 123
# 输出：321
# 
# 
# 示例 2：
# 
# 
# 输入：x = -123
# 输出：-321
# 
# 
# 示例 3：
# 
# 
# 输入：x = 120
# 输出：21
# 
# 
# 示例 4：
# 
# 
# 输入：x = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 
# 
# 
#

# @lc code=start
# class Solution:
#     def reverse(self, x: int) -> int:
#         if x == 0:
#             return 0
#         res = 0
#         nx = abs(x)
#         sig = nx//x
#         while nx >= 1:
#             nx, b = divmod(nx, 10)
#             res = res*10 +b
#         res *= sig
#         if res > 2147483647 or res < -2147483648:
#             return 0
#         return res
import operator
class Solution:
    def reverse(self, x: int) -> int:
        sig = int((operator.ge(x, 0)-0.5)*2)
        r = "%d"%(sig*x)
        r = int(r[::-1])
        return sig*r*(r<2**31)
# @lc code=end

