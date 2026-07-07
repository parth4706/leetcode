class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        k = 0
        c = 0
        flowerbed.insert(0,0)
        flowerbed.append(0)

        for i in flowerbed:
            if i == 0:
                c += 1
            else:
                c = 0
            if c >= 3:
                k += 1
                c = 1
        return k >= n
