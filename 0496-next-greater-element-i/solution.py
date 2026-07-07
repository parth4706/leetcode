class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        k = len(nums2)
        def f(x):
            n = nums2.index(x)
            if n == -1:
                return -1
            for i in range(n,k):
                if nums2[i] > x:
                    return nums2[i]
            else:
                return -1
        for i in nums1:
            res.append(f(i))
        return res

