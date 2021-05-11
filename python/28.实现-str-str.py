#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == None or len(needle) == 0:
            return 0
        end = len(needle)-1
        for i in range(len(haystack)-end):
            for j in range(end + 1):
                if haystack[i+j] != needle[j]:
                    break
                if j == end:
                    return i
        return -1
    def strStr1(self, haystack: str, needle: str) -> int:
        # time too long
        if needle == None or len(needle) == 0:
            return 0
        candidate = []
        end = len(needle)-1
        for cur in range(len(haystack)):
            c = haystack[cur]
            if c == needle[0]:
                candidate.append(cur)
            cid = 0
            while cid < len(candidate):
                head = cur-candidate[cid]
                if c != needle[head]:
                    candidate.pop(cid)
                elif head == end:
                    return candidate[cid]
                else:
                    cid += 1
        return -1
# @lc code=end