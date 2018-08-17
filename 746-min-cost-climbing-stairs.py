class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # DP
        p2, p1 = cost[:2]
        for i in range(2, len(cost)):
            # get the min cost when reach i th step
            p2, p1 = p1, min(p2,p1)+cost[i]
        return min(p2,p1)
