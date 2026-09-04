class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        idx = 0
        m = 0
        res = 0
        min_arr = []
        if not nums:
            return 0
        

        mi = nums[-1]
        for i in nums[::-1]:
            if mi > i:
                mi = i
            min_arr.append(mi)
        for i in nums:
            if m< i:
                m = i
            if m -min_arr[len(min_arr)-1 - idx] <= k:
                return idx
            idx += 1 

        return -1
