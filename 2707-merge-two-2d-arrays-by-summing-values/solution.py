class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        m = max(nums1[-1][0],nums2[-1][0])
        x = [0]*(m+1)
        for i in nums1:
            x[i[0]] += i[1]
        for i in nums2:
            x[i[0]] += i[1]
        for i in range(m+1):
            if x[i] != 0:
                res.append([i,x[i]])
        return res

