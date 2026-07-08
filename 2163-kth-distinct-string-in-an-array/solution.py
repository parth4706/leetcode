class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        for i in arr:
            if arr.count(i) == 1:
                k -= 1
            if k == 0:
                return i
        return ""
