import math
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if complexity.count(min(complexity)) == 1 and min(complexity)==complexity[0]:
            return math.factorial(len(complexity)-1)%(10**9 +7)
        return 0
