class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_num(n):
            """
            :typr n:int
            :rtype list[int]
            """
            re = []
            while n > 9:
                re.append(n%10)
                n /= 10
            re.append(n)
            return re
        
        result = n
        while result != 1:
            if result == 4:
                return False
            num = get_num(result)
            result = 0
            for i in num:
                result += i**2
        return True
            
