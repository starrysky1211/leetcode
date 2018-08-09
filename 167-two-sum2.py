class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # in order to use the information of 'sorted', i got two solutions: 
        # 1. traversal the list like two-sum until the num > target.
        # 2. traversal the list until the num > (target+1 // 2),
        # after get a num, binary search target-num between index from i to last_search_index,
        # last_search_index is the last index while searching target-num
        
        # now, we first make a binary search function
        def bi_search(numbers, low, high, val):
             """
             :type numbers: List[int]
             :type low: int
             :type high: int
             :type val: int
             :rtype: turple[0/1, int]
             """
             while low <= high:
                 mid = (high+low)/2
                 if numbers[mid] == val:
                     return (1, mid)
                 elif numbers[mid] > val:
                     high = mid - 1
                 else:
                     low = mid + 1
             return (0, low)
        n = len(numbers)
        high = n - 1
        for i in range(n):
             if numbers[i] > (target + 1) // 2:
                 return []
             re = bi_search(numbers, i+1, high, target-numbers[i])
             if re[0]:
                 return (i+1, re[1]+1)
             else:
                 high = re[1]
            
