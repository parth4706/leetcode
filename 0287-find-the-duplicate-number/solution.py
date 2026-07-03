class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        my_counter = Counter(nums)
        element, count = my_counter.most_common(1)[0]
        return element
        
