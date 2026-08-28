class Solution(object):
    def asteroidCollision(self, asteroids):
        stk = []

        for x in asteroids:
            while stk and x < 0 and stk[-1] > 0 and stk[-1] < -x:
                stk.pop()

            if not stk or x > 0 or stk[-1] < 0:
                stk.append(x)
            elif stk[-1] == -x:
                stk.pop()

        return stk
