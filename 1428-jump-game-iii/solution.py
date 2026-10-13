class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        vis = set()
        def f(i):
            if i in vis:
                return False
            vis.add(i)
            if i >= len(arr) or i < 0:
                return False
            if arr[i] == 0:
                return True
            
            return f(i+arr[i]) or f(i-arr[i])
        return f(start)

