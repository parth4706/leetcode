class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        Count = 0
        for i in hours:
            if i >= target:
                Count +=1
        return Count
