class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for i in points:
            i.append(float(i[0]**2+i[1]**2)**0.5)
        points.sort(key=lambda x: x[2])
        for i in points:
            i.pop()
        return points[:k]
