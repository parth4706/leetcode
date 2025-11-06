class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        l = Counter(s)

        odd = float('-inf')   # track max odd frequency
        even = float('inf')   # track min even frequency

        for i in l:
            if l[i] % 2 == 1:   # odd frequency
                odd = max(odd, l[i])

        for i in l:
            if l[i] % 2 == 0:   # even frequency
                even = min(even, l[i])

        # handle edge cases: if no odd or no even found
        if odd == float('-inf') or even == float('inf'):
            return 0

        return odd - even
