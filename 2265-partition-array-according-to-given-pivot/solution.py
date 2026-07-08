class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        res1 = []
        res2=[]
        for i in nums:
            if i > pivot:
                res1.append(i)
            elif i == pivot:
                continue
            else:
                res2.append(i)
        return res2 + [pivot]*(nums.count(pivot)) + res1

        
