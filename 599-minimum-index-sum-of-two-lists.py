class Solution1(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        h = [['',float('inf')]]
        for i in range(len(list1)):
            r = list1[i]
            for j in range(len(list2)):
                if r == list2[j]:
                    if i+j < h[0][1]:
                        h = [[r,i+j]]
                    elif i+j == h[0][1]:
                        h.append([r,i+j])
                    break
        return [i[0] for i in h]
# can be faster using the same method

class Solution2(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        msum = len(list1) + len(list2)
        res = []
        for i, v in enumerate(list1):
            d[v] = i
        
        for i, v in enumerate(list2):
            if v in d:
                if d[v] + i == msum:
                    res.append(v)
                elif d[v] + i < msum:
                    msum = d[v] + i
                    res = [v]
        
        return res
