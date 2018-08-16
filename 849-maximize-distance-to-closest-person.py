class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        blank = 0
        l = 0
        head = 0
        if seats[0] == 0:
            for i in seats:
                if i == 1:
                    break
                head += 1
        for i in range(len(seats)):
            if seats[i] == 0:
                blank += 1
            else:
                l = max(l, blank)
                blank = 0
        tail = blank
        print tail
        return max((l+1)//2, head, tail)
