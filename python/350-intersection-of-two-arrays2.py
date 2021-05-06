class Solution1(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash1 = {}
        hash2 = {}
        for i in nums1:
            hash1[i] = hash1.get(i,0) + 1
        for j in nums2:
            hash2[j] = hash2.get(j,0) + 1
        re = []
        for k in hash1:
            if k in hash2:
                re+=[k]*min(hash1[k], hash2[k])
        return re
# using hashtable beat 39%
# a faster way using one hashtable
class Solution2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        re = []
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        for i in nums1:
             hashmap[i] = hashmap.get(i,0) + 1
        for j in nums2:
            if j in hashmap and hashmap[j]>0:
                re.append(j)
                hashmap[j] -= 1
        return re
