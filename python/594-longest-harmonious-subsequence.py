class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            h[i] = h.get(i,0) + 1
        # v = sorted(h.keys())
        # max_ = 0
        # for i in range(1,len(v)):
        #     if v[i]-v[i-1] == 1:
        #         max_ = max(max_,h[v[i]]+h[v[i-1]])
        max_ = 0
        for k in h:
            if k+1 in h:
                max_ = max(max_,h[k]+h[k+1])
        
        return max_
            
