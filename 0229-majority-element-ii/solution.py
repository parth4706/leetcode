from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = Counter(nums)
        k =set()
        n = len(nums)
        for i in l:
            if l[i] > n/3:
                k.add(i)
        return list(k)
