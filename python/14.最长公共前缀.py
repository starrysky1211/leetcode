#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        preflix = strs[0]
        p_len = len(preflix)
        for s in strs[1:]:
            h_len = len(s)
            shortest_len = min(p_len, h_len)
            # if shortest_len == 0:
            #     return ""
            finished = True
            for i in range(shortest_len):
                if preflix[i] != s[i]:
                    if i == 0:
                        finished = False
                        return ""
                    else:
                        preflix = preflix[:i]
                        p_len = i
                        finished = False
                        break
                
            if finished:
                preflix = s[:shortest_len]
                p_len = shortest_len
        return preflix
# @lc code=end

