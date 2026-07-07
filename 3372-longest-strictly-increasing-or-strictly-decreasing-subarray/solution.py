class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        d = 1
        m_i = 1
        m_d = 1
        for j in range(len(nums)-1):
            if nums[j] < nums[j+1]:
                i += 1
                m_i = max(m_i,i)
            else:
                i = 1
            if nums[j] > nums[j+1]:
                d += 1
                m_d = max(m_d,d)
            else:
                d = 1
        return max(m_d,m_i)
            
