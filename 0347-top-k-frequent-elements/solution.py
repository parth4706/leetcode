from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = Counter(nums)
        lst = [[x,r] for x,r in C.items()]
        lst = sorted(lst,key = lambda x: x[1],reverse = True)
        res = []
        for i in range(k):
            res.append(lst[i][0])
        return res
