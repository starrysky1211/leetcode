class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = [1]*n
        prime[:2] = [0,0]
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                prime[i*i : n : i] = [0]*len(prime[i*i : n : i])
        return sum(prime)
        
