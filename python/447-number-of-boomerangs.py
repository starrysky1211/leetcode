class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dis(p1,p2):
            """
            :type p1,p2:List[int,int]
            :rtype int
            """
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        n = len(points)
        res = 0
        for i in range(n):
            d = {}
            for j in range(n):
                if i==j:
                    continue
                di = dis(points[i],points[j])
                d[di] = d.get(di,0)+1
            for v in d.values():
                res += (v-1)*v
        return res
