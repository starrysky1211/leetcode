class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # 连续的n个0，可以找到(n-1)//2个空位，先遍历整个数组，输出所有的相邻零的个数，然后map，sum即可
        count = 1
        zeros = []
        for i in flowerbed:
            if i == 0:
                count += 1
            else:
                zeros.append(count)
                count = 0
        zeros.append(count+1)
        top = sum([max((j-1)//2,0) for j in zeros])
        print top
        if n <= top:
            return True
        else:
            return False
