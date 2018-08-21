class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        for o in cpdomains:
            t, web = o.split()
            web = web.split('.')
            for i in range(len(web)):
                s = '.'.join(web[-i:])
                d[s] = d.get(s,0)+int(t)
        res = []
        for i in d:
            res.append(str(d[i])+' '+i)
        return res
