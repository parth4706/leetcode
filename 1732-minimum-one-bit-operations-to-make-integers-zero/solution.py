class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def helper(x):
            if x == 0:
                return 0
            m = x.bit_length() - 1
            return (1 << (m + 1)) - 1 - helper(x ^ (1 << m))
        
        return helper(n)
