from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        sol = []
        for i in c1:
            if i in c2:
                for j in range(min(c1[i],c2[i])):
                    sol.append(i)
        return sol
