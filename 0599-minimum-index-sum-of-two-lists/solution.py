class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {restaurant: i for i, restaurant in enumerate(list2)}
        res = []
        min_sum = float('inf')

        for i, restaurant in enumerate(list1):
            if restaurant in index_map:
                j = index_map[restaurant]
                s = i + j
                if s < min_sum:
                    min_sum = s
                    res = [restaurant]
                elif s == min_sum:
                    res.append(restaurant)

        return res
