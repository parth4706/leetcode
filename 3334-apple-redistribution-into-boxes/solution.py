class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        A = 0
        S = sum(apple)
        i =0
        while A < S:
            A += capacity[i]
            i+=1
        return i
