class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        m = 0
        for i in sentences:
            if i == "":
                continue
            m = max(m,i.count(" ")+1)
        return m

