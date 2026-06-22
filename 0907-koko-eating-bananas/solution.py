class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def test(k):
            hours=0
            for i in piles:
                hours += ceil(i/k)
                
            return hours <= h
        l = 1
        r = max(piles)
        while l<r:
            m = (l +r)//2
            if test(m):
                r = m
            else:
                l = m +1
        return l
