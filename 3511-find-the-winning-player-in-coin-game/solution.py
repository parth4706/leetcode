class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        turns = min(x,y//4)
        if turns%2==0:
            return "Bob"
        else:
            return "Alice"
