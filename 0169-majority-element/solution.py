from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = Counter(nums)
        s = [(x, y) for x, y in k.items()]
        s = sorted(s,key=lambda x: x[1],reverse = True)
        return s[0][0]

