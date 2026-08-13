from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])
        seen = {beginWord}

        while q:
            word, dist = q.popleft()

            if word == endWord:
                return dist

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":

                    newWord = word[:i] + c + word[i + 1:]

                    if newWord in words and newWord not in seen:
                        seen.add(newWord)
                        q.append((newWord, dist + 1))

        return 0
