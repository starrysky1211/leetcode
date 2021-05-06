class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fi, se, th = None, None, None
        for i in range(len(nums)):
            if nums[i] in [fi, se, th]:
                continue
            elif not fi or nums[i] > fi:
                th = se
                se = fi
                fi = nums[i]
            elif not se or nums[i] > se:
                th = se
                se = nums[i]
            elif not th or nums[i] > th:
                th = nums[i]
        return th if th != None else fi
