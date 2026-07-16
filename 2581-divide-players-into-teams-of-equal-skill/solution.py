class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        n = len(skill)
        s = 0
        for i in range(len(skill)//2):
            if skill[i]+skill[n-i-1]!= skill[i+1]+skill[n-i-2]:
                return -1
            s += skill[i]*skill[n-i-1]
        return s
