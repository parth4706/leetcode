class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = nums1 + nums2
        s.sort()
        if len(s)%2 == 0:
            median = (s[len(s)//2] + s[len(s)//2-1])/2
        else:
            median = s[len(s)//2]    
        return median
