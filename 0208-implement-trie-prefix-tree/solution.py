class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        d = self.trie
        for i in word:
            if i not in d:
                d[i] = {}
            d = d[i]
        d['.'] = '.'
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        d = self.trie
        for i in word:
            if i not in d:
                return False
            d = d[i]
        if '.' in d:
            return True
        return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        d = self.trie
        for i in prefix:
            if i not in d:
                return False
            d = d[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
